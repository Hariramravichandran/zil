CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


CREATE TABLE IF NOT EXISTS public.expenses_cat
(
    expense_id uuid NOT NULL DEFAULT uuid_generate_v4(),
    category text COLLATE pg_catalog."default",
    CONSTRAINT expenses_cat_pkey PRIMARY KEY (expense_id)
);


CREATE TABLE IF NOT EXISTS public.expenses
(
    exp_id uuid,
    name text COLLATE pg_catalog."default",
    amount double precision,
    date date
)