create type order_side as enum('buy','sell');
create type order_status as enum('open','partial,'filled','cancelled');

create table orders(
    id serial primary key,
    user_id integer not null references users(id) on delete cascade,
    asset_id integer not null references assets(id),
    side order_side not null,
    price numeric(30,18) not null check(price > 0),
    amount numeric(30,18) not null check(amount > 0),
    filled numeric(30,18) not null default 0 check(filled >= 0 and filled <= amount),
    status order_status not null default 'open',
    created_at timestamp with time zone not null default now(),
    updated_at timestamp with time zone not null default now()
);