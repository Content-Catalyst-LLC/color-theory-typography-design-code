#!/usr/bin/env Rscript
inventory <- read.csv("data/article_inventory.csv", stringsAsFactors = FALSE)
outdir <- file.path("calculators", "outputs")
dir.create(outdir, recursive = TRUE, showWarnings = FALSE)
summary <- as.data.frame(table(inventory$section), stringsAsFactors = FALSE)
names(summary) <- c("section", "article_count")
write.csv(summary, file.path(outdir, "section_count_summary.csv"), row.names = FALSE)
cat("Wrote section count summary.\n")
