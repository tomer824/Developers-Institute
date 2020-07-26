SELECT COUNT(actor_id)
FROM actors

INSERT INTO actors (first_name)
VALUES ('Tom');

ERROR:  null value in column "last_name" violates not-null constraint
DETAIL:  Failing row contains (5, Tom, null, null, null).
SQL state: 23502