create extension if not exists pgcrypto;

create table if not exists profiles (
    id uuid primary key default gen_random_uuid(),
    name text not null,
    email text,
    phone text,
    location text,
    education text,
    experience_years numeric default 0,
    created_at timestamptz default now()
);

create table if not exists preferences (
    id uuid primary key default gen_random_uuid(),
    profile_id uuid references profiles(id) on delete cascade,
    target_roles text[],
    target_locations text[],
    excluded_roles text[],
    minimum_match_score integer default 70,
    created_at timestamptz default now()
);

create table if not exists jobs (
    id uuid primary key default gen_random_uuid(),
    source text not null,
    external_id text,
    title text not null,
    company text,
    location text,
    url text,
    description text,
    salary_min numeric,
    salary_max numeric,
    posted_at timestamptz,
    discovered_at timestamptz default now(),
    match_score integer,
    match_reason text,
    status text default 'new',
    created_at timestamptz default now(),
    unique(source, external_id)
);

create table if not exists resumes (
    id uuid primary key default gen_random_uuid(),
    name text not null,
    role_type text,
    content text,
    created_at timestamptz default now()
);

create table if not exists applications (
    id uuid primary key default gen_random_uuid(),
    job_id uuid references jobs(id) on delete cascade,
    resume_id uuid references resumes(id),
    status text default 'prepared',
    cover_letter text,
    application_answers jsonb,
    applied_at timestamptz,
    interview_date timestamptz,
    notes text,
    created_at timestamptz default now()
);
