CREATE DATABASE IF NOT EXISTS recommendation_db;

USE recommendation_db;

CREATE TABLE IF NOT EXISTS recommendations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(100),
    reason TEXT
);

INSERT INTO recommendations (product, reason) VALUES
('Credit Card', 'High rewards for spending'),
('Investment Fund', 'Low risk, steady growth'),
('Personal Loan', 'Flexible repayment'),
('Mortgage', 'Long-term investment'),
('Insurance', 'Risk protection');
