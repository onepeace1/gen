CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    news_date TIMESTAMP WITH TIME ZONE,
    news_ranking INT,
    category TEXT,
    url TEXT,
    img_url TEXT,
    title TEXT,
    content_summarize TEXT,
    content TEXT
);
