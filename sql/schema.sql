CREATE TABLE IF NOT EXISTS articles (
    article_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    section TEXT NOT NULL,
    sequence_order INTEGER NOT NULL,
    slug TEXT NOT NULL,
    status TEXT DEFAULT 'planned'
);

CREATE TABLE IF NOT EXISTS references_harvard (
    reference_id TEXT PRIMARY KEY,
    author TEXT,
    year TEXT,
    title TEXT NOT NULL,
    publisher_or_source TEXT,
    url TEXT,
    notes TEXT
);
