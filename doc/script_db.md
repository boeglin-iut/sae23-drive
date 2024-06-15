Pour créer les tables dans la base de données :
```
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    descriptif TEXT
);

CREATE TABLE clients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_inscription DATE,
    adresse TEXT
);

CREATE TABLE produits (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    date_de_peremption DATE,
    photo VARCHAR(255), 
    marque VARCHAR(100),
    prix DECIMAL(10, 2),
    id_categorie INT,
    FOREIGN KEY (id_categorie) REFERENCES categories(id) ON DELETE CASCADE
);

CREATE TABLE commandes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_client INT,
    date DATE,
    FOREIGN KEY (id_client) REFERENCES clients(id) ON DELETE CASCADE
);

CREATE TABLE liste_produit (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_commande INT,
    id_produit INT,
    quantite INT,
    FOREIGN KEY (id_commande) REFERENCES commandes(id) ON DELETE CASCADE,
    FOREIGN KEY (id_produit) REFERENCES produits(id) ON DELETE CASCADE
);
```

¨Pour insérer des données dans les tables :
```
INSERT INTO categories (nom, descriptif) VALUES
('Fruits', 'Fruits frais et de saison'),
('Légumes', 'Légumes frais et de saison'),
('Viandes', 'Viandes fraîches et surgelées'),
('Produits laitiers', 'Produits laitiers et dérivés'),
('Boissons', 'Boissons chaudes et froides');

INSERT INTO clients (nom, prenom, date_inscription, adresse) VALUES
('Dupont', 'Pierre', '2020-01-01', '123 rue de la République'),
('Martin', 'Marie', '2020-02-01', '456 avenue des Champs-Élysées'),
('Lefebvre', 'Jean', '2020-03-01', '789 rue de Rivoli'),
('Garcia', 'Sophie', '2020-04-01', '321 rue de la Paix'),
('Bertrand', 'François', '2020-05-01', '901 boulevard Saint-Michel');

INSERT INTO produits (nom, date_de_peremption, photo, marque, prix, id_categorie) VALUES
('Pomme', '2023-02-28', 'pomme.jpg', 'Granny Smith', 1.99, 1),
('Carotte', '2023-03-15', 'carotte.jpg', 'Ferme Bio', 0.99, 2),
('Poitrine de poulet', '2023-04-10', 'poulet.jpg', 'Tyson', 8.99, 3),
('Lait', '2023-05-01', 'lait.jpg', '2% Bio', 2.49, 4),
('Coca-Cola', '2023-06-01', 'coke.jpg', 'Coca-Cola', 1.99, 5),
('Banane', '2023-02-20', 'banane.jpg', 'Chiquita', 0.59, 1),
('Steak de boeuf', '2023-04-20', 'boeuf.jpg', 'Angus', 14.99, 3);

INSERT INTO commandes (id_client, date) VALUES
(1, '2024-01-01'),
(2, '2024-01-15'),
(3, '2024-02-01'),
(1, '2024-02-15'),
(4, '2024-03-01');

INSERT INTO liste_produit (id_commande, id_produit, quantite) VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 1),
(3, 4, 2),
(4, 5, 1),
(4, 1, 1),
(5, 6, 3);
```