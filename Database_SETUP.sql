-- Create the images table
CREATE TABLE images (
	image_id SERIAL PRIMARY KEY,
	file_path TEXT NOT NULL,
	file_size BIGINT NOT NULL,
	image_width INT NOT NULL,
	image_height INT NOT NULL,
	upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	description TEXT
);


