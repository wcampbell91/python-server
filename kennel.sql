INSERT INTO `Animal` VALUES (null, "Daps", "Kennel", "Boxer", 2, 2);

INSERT INTO Animal (
    id,
    name,
    status,
    breed,
    customer_id,
    location_id
  )
VALUES (
    id:INTEGER,
    'name:TEXT',
    'status:TEXT',
    'breed:TEXT',
    customer_id:INTEGER,
    location_id:INTEGER
  );
  
    SELECT 
        a.id,
        a.name,
        a.breed,
        a.status,
        a.location_id,
        a.customer_id,
        l.name location_name,
        l.address location_address,
        c.name customer_name,
        c.address customer_address,
        c.email customer_email,
        c.password customer_password
    FROM Animal a
    JOIN Location l
        ON l.id = a.location_id
    JOIN Customer c
        ON c.id = a.customer_id
