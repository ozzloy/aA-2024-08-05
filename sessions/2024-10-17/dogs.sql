CREATE TABLE puppies (
  name VARCHAR(50),
  age_yrs NUMERIC(3,1),
  breed VARCHAR(100),
  weight_lbs INTEGER,
  microchipped BOOLEAN
);

INSERT
 INTO
 puppies
 (name, age_yrs, breed, weight_lbs, microchipped)
VALUES
  (  'Cooper', 1  , 'Miniature Schnauzer', 18, 1),
  (   'Indie', 0.5,   'Yorkshire Terrier', 13, 1),
  (    'Kota', 0.7, 'Australian Shepherd', 26, 0),
  (     'Zoe', 0.8,        'Korean Jindo', 32, 1),
  ( 'Charley', 1.5,        'Basset Hound', 25, 0),
  ('Ladybird', 0.6,         'Labradoodle', 20, 1),
  (  'Callie', 0.9,               'Corgi', 16, 0),
  (  'Jaxson', 0.4,              'Beagle', 19, 1),
  (  'Leinni', 1  , 'Miniature Schnauzer', 25, 1),
  (     'Max', 1.6,     'German Shepherd', 65, 0);

SELECT name, breed FROM puppies
 WHERE breed = 'Miniature Schnauzer';
