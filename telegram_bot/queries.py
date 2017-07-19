SELECT_TRANSLATES = '''
SELECT trans_w FROM words WHERE _id_w != ?
'''

SELECT_WORD = '''
SELECT * FROM words WHERE _id_w = ?
'''

SELECT_SPANISH = '''
SELECT word, sound FROM words WHERE UPPER(trans_w) like UPPER(?)
'''

INSERT_WORD = '''
INSERT INTO words (word, trans_w) VALUES (?, ?)
'''