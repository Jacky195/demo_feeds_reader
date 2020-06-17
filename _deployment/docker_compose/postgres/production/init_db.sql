CREATE USER feeds_reader with encrypted password 'sefdKJHGDedsfq21';
ALTER USER feeds_reader CREATEDB;
CREATE DATABASE feeds_reader;
GRANT ALL PRIVILEGES ON DATABASE feeds_reader TO feeds_reader;
