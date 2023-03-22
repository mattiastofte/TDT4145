INSERT INTO Vogntype (VognNavn) VALUES
('SJ-sittevogn-1'),
('SJ-sovevogn-1');

INSERT INTO Vogntog (VognTogID) VALUES
(1),
(2),
(3);

INSERT INTO Togrute (RuteID, OperatørNavn, VognTogID) VALUES 
(1, 'SJ', 1),
(2, 'SJ', 2),
(3, 'SJ', 3);

INSERT INTO Vogn (VognID, VognNavn) VALUES
(1, 'SJ-sittevogn-1'),
(2, 'SJ-sittevogn-1'),
(3, 'SJ-sittevogn-1'),
(4, 'SJ-sovevogn-1'),
(5, 'SJ-sittevogn-1');

INSERT INTO BestårAv (VognId, VognTogID) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 3);

INSERT INTO Sete (SeteNr, RadNr, VognNavn) VALUES
(1, 1, 'SJ-sittevogn-1'),
(2, 1, 'SJ-sittevogn-1'),
(3, 1, 'SJ-sittevogn-1'),
(4, 1, 'SJ-sittevogn-1'),
(5, 2, 'SJ-sittevogn-1'),
(6, 2, 'SJ-sittevogn-1'),
(7, 2, 'SJ-sittevogn-1'),
(8, 2, 'SJ-sittevogn-1'),
(9, 3, 'SJ-sittevogn-1'),
(10, 3, 'SJ-sittevogn-1'),
(11, 3, 'SJ-sittevogn-1'),
(12, 3, 'SJ-sittevogn-1');

INSERT INTO Seng (SengNr, KupeNr, VognNavn) VALUES
(1, 1, 'SJ-sovevogn-1'),
(2, 1, 'SJ-sittevogn-1'),
(3, 2, 'SJ-sittevogn-1'),
(4, 2, 'SJ-sittevogn-1'),
(5, 3, 'SJ-sittevogn-1'),
(6, 3, 'SJ-sittevogn-1'),
(7, 4, 'SJ-sittevogn-1'),
(8, 4, 'SJ-sittevogn-1');

INSERT INTO Operatør (Navn) VALUES
('SJ');

INSERT INTO KjørerPå (RuteID, Navn) VALUES
(1, 'Nordlandsbanen'),
(2, 'Nordlandsbanen'),
(3, 'Nordlandsbanen');

INSERT INTO Ruteforekomst (Ukedag, RuteID) VALUES 
('Mandag', 1),
('Tirsdag', 1),
('Onsdag', 1),
('Torsdag', 1),
('Fredag', 1),
('Mandag', 2),
('Tirsdag', 2),
('Onsdag', 2),
('Torsdag', 2),
('Fredag', 2),
('Lørdag', 2),
('Søndag', 2),
('Mandag', 3),
('Tirsdag', 3),
('Onsdag', 3),
('Torsdag', 3),
('Fredag', 3);

INSERT INTO RuteTabell (TabellID, Jernbanestasjon, AvgangsTid, AnkomstTid) VALUES
(1, 'Trondheim', '07:49', NULL),
(1, 'Steinkjer', '09:51', '09:51'),
(1, 'Mosjøern', '13:20', '13:20'),
(1, 'Mo i Rana', '14:31', '14:31'),
(1, 'Fauske', '16:49', '16:49'),
(1, 'Bodø',  NULL, '17:34'),
(2, 'Trondheim', '23:05', NULL),
(2, 'Steinkjer', '00:57', '00:57'),
(2, 'Mosjøern', '04:41', '04:41'),
(2, 'Mo i Rana', '05:55', '05:55'),
(2, 'Fauske', '08:19', '08:19'),
(2, 'Bodø',  NULL, '09:05'),
(3, 'Mo i Rana', '08:11', NULL),
(3, 'Mosjøen', '09:14', '09:14'),
(3, 'Steinkjer', '12:31', '12:31'),
(3, 'Trondheim', NULL, '14:13');

INSERT INTO HarRute (RuteID, TabellID) VALUES
(1, 1),
(2, 2),
(3, 3);

