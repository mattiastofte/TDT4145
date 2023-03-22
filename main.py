import sqlite3

# Accepts the path to the database connection
def create_connection(path):
    connection = None
    try:
        # Connect to the database
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("data/train-network.sqlite")

with open('migrations/CreateTables.sql', 'r') as file:
    create_tables = file.read()
    sqlCommands = create_tables.split(';')

    for command in sqlCommands:
        try:
            execute_query(connection, command)  
        except Error as e:
            print("Command skipped: ", e)

# check if a jernbanestasjon exists
jernbanestasjoner = connection.cursor().execute("SELECT * from Jernbanestasjon")

if jernbanestasjoner.fetchone() is None:
    with open('migrations/CreateNordlandsbane.sql', 'r') as file:
        create_nordlandsbane = file.read()
        sqlCommands = create_nordlandsbane.split(';')

        for command in sqlCommands:
            try:
                execute_query(connection, command)  
            except Error as e:
                print("Command skipped: ", e)
else:
    print("Jernbanestasjon table is not empty")
    
togruter = connection.cursor().execute("SELECT * from Togrute")

if togruter.fetchone() is None:
    with open('migrations/CreateTrainroutes.sql', 'r') as file:
        create_trainroutes = file.read()
        sqlCommands = create_trainroutes.split(';')

        for command in sqlCommands:
            try:
                execute_query(connection, command)  
            except Error as e:
                print("Command skipped: ", e)

print(">> --------- [Train system] --------- <<")
print("")
print("Hvilken operasjon ønsker du å utføre?")
print("")
print("[1] Finn togruter som går fra en gitt stasjon på en gitt ukedag")
print("")
operation = input("")
if int(operation) == 1:
    print("Enter the name of the station: ")
    station = input("")
    print("Enter the weekday: ")
    weekday = input("")
    result = connection.cursor().execute(f"SELECT DISTINCT Togrute.RuteID, Operatør.Navn AS OperatørNavn FROM Togrute JOIN Operatør ON Togrute.OperatørNavn = Operatør.Navn JOIN Ruteforekomst ON Togrute.RuteID = Ruteforekomst.RuteID JOIN HarRute ON Togrute.RuteID = HarRute.RuteID JOIN RuteTabell ON HarRute.TabellID = RuteTabell.TabellID WHERE Ruteforekomst.Ukedag = '{weekday}' AND RuteTabell.Jernbanestasjon = '{station}';")
    print(result.fetchall())

"""

SELECT DISTINCT Togrute.RuteID, Operatør.Navn AS OperatørNavn
FROM Togrute
JOIN Operatør ON Togrute.OperatørNavn = Operatør.Navn
JOIN Ruteforekomst ON Togrute.RuteID = Ruteforekomst.RuteID
JOIN HarRute ON Togrute.RuteID = HarRute.RuteID
JOIN RuteTabell ON HarRute.TabellID = RuteTabell.TabellID
WHERE Ruteforekomst.Ukedag = '<UKEDAG>'
AND RuteTabell.Jernbanestasjon = '<STASJONSNAVN>';
"""
"""

2023-03-23

WITH RuteForekomsterForToDager AS (
  SELECT RuteID
  FROM Ruteforekomst
  WHERE Ukedag IN (strftime('%w', 'YYYY-MM-DD'), strftime('%w', 'YYYY-MM-DD', '+1 day')) -- Erstatt 'YYYY-MM-DD' med den aktuelle datoen
),

RuterMedAvgang AS (
  SELECT hr.RuteID, rt.Jernbanestasjon AS StartStasjon, rt.AvgangsTid,
    CASE
      WHEN strftime('%w', 'YYYY-MM-DD') = strftime('%w', 'YYYY-MM-DD', '+1 day') THEN 1
      ELSE 0
    END AS NesteDag
  FROM HarRute hr
  JOIN RuteTabell rt ON hr.TabellID = rt.TabellID
  WHERE rt.Jernbanestasjon = 'StartStasjon' -- Erstatt 'StartStasjon' med den aktuelle startstasjonen
  AND (
    (time(rt.AvgangsTid) >= time('HH:MM') AND strftime('%w', rt.AvgangsTid) = strftime('%w', 'YYYY-MM-DD')) -- Erstatt 'HH:MM' med det aktuelle klokkeslettet
    OR strftime('%w', rt.AvgangsTid) = strftime('%w', 'YYYY-MM-DD', '+1 day')
  )
  AND hr.RuteID IN RuteForekomsterForToDager
),

RuterMedAnkomst AS (
  SELECT hr.RuteID, rt.Jernbanestasjon AS SluttStasjon, rt.AnkomstTid
  FROM HarRute hr
  JOIN RuteTabell rt ON hr.TabellID = rt.TabellID
  WHERE rt.Jernbanestasjon = 'SluttStasjon' -- Erstatt 'SluttStasjon' med den aktuelle sluttstasjonen
  AND hr.RuteID IN RuteForekomsterForToDager
)

SELECT rma.RuteID, rma.SluttStasjon, rma.AnkomstTid, rmd.StartStasjon, rmd.AvgangsTid, rmd.NesteDag
FROM RuterMedAvgang rmd
JOIN RuterMedAnkomst rma ON rmd.RuteID = rma.RuteID
WHERE time(rma.AnkomstTid) > time(rmd.AvgangsTid)
ORDER BY rmd.NesteDag ASC, rmd.AvgangsTid ASC;



"""


"""

a) Databasen skal kunne registrere data om alle jernbanestrekninger i Norge. Dere skal legge inn
data for Nordlandsbanen (som vist i figuren). Dette kan gjøres med et skript, dere trenger ikke å
programmere støtte for denne funksjonaliteten.

b) Dere skal kunne registrere data om togruter. Dere skal legge inn data for de tre togrutene på
Nordlandsbanen som er beskrevet i vedlegget til denne oppgave. Dette kan gjøres med et skript,
dere trenger ikke å programmere støtte for denne funksjonaliteten.

c) For en stasjon som oppgis, skal bruker få ut alle togruter som er innom stasjonen en gitt ukedag.
Denne funksjonaliteten skal programmeres.

d) Bruker skal kunne søke etter togruter som går mellom en startstasjon og en sluttstasjon, med
utgangspunkt i en dato og et klokkeslett. Alle ruter den samme dagen og den neste skal
returneres, sortert på tid. Denne funksjonaliteten skal programmeres.

e) En bruker skal kunne registrere seg i kunderegisteret. Denne funksjonaliteten skal programmeres.

f) Det skal legges inn nødvendige data slik at systemet kan håndtere billettkjøp for de tre togrutene
på Nordlandsbanen, mandag 3. april og tirsdag 4. april i år. Dette kan gjøres med et skript, dere
trenger ikke å programmere støtte for denne funksjonaliteten.

g) Registrerte kunder skal kunne finne ledige billetter for en oppgitt strekning på en ønsket togrute
og kjøpe de billettene hen ønsker. Denne funksjonaliteten skal programmeres.
• Pass på at dere bare selger ledige plasser

h) For en bruker skal man kunne finne all informasjon om de kjøpene hen har gjort for fremtidige
reiser. Denne funksjonaliteten skal programmeres.

"""