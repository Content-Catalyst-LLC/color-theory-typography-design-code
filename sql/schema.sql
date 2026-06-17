DROP TABLE IF EXISTS article_inventory;
DROP TABLE IF EXISTS sibling_article_maps;
CREATE TABLE article_inventory (section TEXT NOT NULL, title TEXT NOT NULL, slug TEXT PRIMARY KEY, status TEXT NOT NULL, website_url TEXT NOT NULL);
CREATE TABLE sibling_article_maps (article_map TEXT NOT NULL, slug TEXT PRIMARY KEY, repo TEXT NOT NULL, website_url TEXT NOT NULL);
