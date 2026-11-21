// Entry program for the make.fun bounty "Post a GTA 6 meme on X".
//
// The post itself is the entry: the house reads it from X. All this
// program has to do is copy POST.json (which names the post's URL)
// from the repository root into the output directory.

import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoDir = process.env.MAKEFUN_BOT_DIR ?? dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const source = join(repoDir, "POST.json");
if (!existsSync(source)) {
  throw new Error(`POST.json not found in the repository (${source})`);
}

mkdirSync(outDir, { recursive: true });
const target = join(outDir, "POST.json");
copyFileSync(source, target);

// Verify the published copy: it must parse and name an X post's URL,
// the two things the house's scorer checks before judging.
const published = JSON.parse(readFileSync(target, "utf8"));
const postUrl = /^https:\/\/(x\.com|twitter\.com)\/[^/]+\/status\/\d+$/;
if (typeof published.url !== "string" || !postUrl.test(published.url)) {
  throw new Error(`published POST.json does not name an X post: ${target}`);
}
console.log(`copied ${source} -> ${target} (post: ${published.url})`);
