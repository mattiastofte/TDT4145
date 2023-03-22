INSERT INTO Jernbanestasjon (Navn, Høyde) VALUES 
('Bodø', 4.1),
('Fauske', 34.0),
('Mo i Rana', 3.5),
('Mosjøen', 6.8),
('Steinkjer', 3.6),
('Trondheim', 5.1);

INSERT INTO GårMellom (StrekningsID, Navn1, Navn2) VALUES
(1, 'Trondheim', 'Steinkjer'),
(2, 'Steinkjer', 'Mosjøen'),
(3, 'Mosjøen', 'Mo i Rana'),
(4, 'Mo i Rana', 'Fauske'),
(5, 'Fauske', 'Bodø');

INSERT INTO Delstrekning (StrekningsID, Lengde, Dobbeltspor) VALUES
(1, 120, 1),
(2, 280, 0),
(3, 90, 0),
(4, 170, 0),
(5, 60, 0);

INSERT INTO Banestrekning (Navn, Elektrisk, HovedretningFra) VALUES
('Nordlandsbanen', 0, 'Trondheim');

INSERT INTO DelAv (Navn, StrekningsID) VALUES
('Nordlandsbanen', 1),
('Nordlandsbanen', 2),
('Nordlandsbanen', 3),
('Nordlandsbanen', 4),
('Nordlandsbanen', 5);
