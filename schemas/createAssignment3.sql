drop table Participator cascade;
create table Participator(
  ID int,
  Name varchar(30),
  Type varchar(30),
  Salary int,
  Support float,
  Contact varchar(20),
  Address varchar(100),
  primary key (ID)
);

drop table Campaign cascade;
create table Campaign(
  ID int,
  Content varchar(100),
  Address varchar(100),
  start_time varchar(100),
  end_time varchar(100),
  primary key (ID)
);

drop table Donors cascade;
create table Donors(
  ID int,
  Name varchar(30),
  Funding float,
  Contact varchar(20),
  Address varchar(100),
  primary key (ID)
);

drop table Advertise cascade;
create table Advertise (
  ID int,
  Method varchar(10) not null ,
  primary key (ID)
);

drop table Working cascade;
create table Working(
  Campaign_ID int,
  Participator_ID int,
  primary key (Campaign_ID, Participator_ID),
  foreign key (Campaign_ID) references Campaign(ID),
  foreign key (Participator_ID) references Participator(ID)
);

drop table Funding cascade;
create table Funding(
  Campaign_ID int,
  Donors_ID int,
  expense float,
  primary key (Campaign_ID, Donors_ID),
  foreign key (Campaign_ID) references Campaign(ID),
  foreign key (Donors_ID) references Donors(ID)
);

drop table Adopt cascade;
create table Adopt(
  Campaign_ID int,
  Advertise_ID int,
  primary key (Campaign_ID, Advertise_ID),
  foreign key (Campaign_ID) references Campaign(ID),
  foreign key (Advertise_ID) references Advertise(ID)
);

insert into Participator values (1, 'John', 'volunteer', Null, Null, '123456789', 'New York');
insert into Participator values (2, 'Jane', 'wroker', 300, Null, '123456789', 'Washington');
insert into Participator values (3, 'Joy', 'worker', 280, Null, '123456789', 'San Diego');
insert into Participator values (4, 'Marry', 'supporter', Null, 1000, '123456789', 'Austin');
insert into Participator values (5, 'May', 'supporter', Null, 1000, '123456789', 'Chicago');
insert into Participator values (6, 'Mike', 'worker', 230, Null, '123456789', 'Boston');
insert into Participator values (7, 'Tom', 'supporter', Null, 1000, '123456789', 'New York');
insert into Participator values (8, 'Ted', 'volunteer', Null, Null, '123456789', 'Boston');
insert into Participator values (9, 'Tony', 'volunteer', Null, Null, '123456789', 'Washington');
insert into Participator values (10, 'Judy', 'volunteer', Null, Null, '123456789', 'New York');
insert into Participator values (11, 'Julia', 'volunteer', Null, Null, '123456789', 'New York');

insert into Campaign values (1, ' Air Pollutio', 'New York', '2019-6-1', '2019-6-30');
insert into Campaign values (2, 'Pollution', 'New York', '2019-7-1', '2019-9-30');
insert into Campaign values (3, ' Air Pollutioe', 'Washington', '2019-6-1', '2019-6-30');
insert into Campaign values (4, 'Environment Protection', 'Washington', '2019-3-1', '2019-3-30');
insert into Campaign values (5, ' Soil and Land Pollutione', 'Chicago', '2019-4-10', '2019-6-30');
insert into Campaign values (6, 'Deforestation', 'Boston', '2019-3-20', '2019-4-30');
insert into Campaign values (7, 'Genetic Modification', 'San Diego', '2019-5-1', '2019-6-30');
insert into Campaign values (8, 'Overpopulation', 'San Diego', '2019-7-1', '2019-7-10');

insert into Donors values (1, 'Google', 1000000, '123456789', 'San Francisco');
insert into Donors values (2, 'Microsoft', 100000, '123456789', 'Seattle');
insert into Donors values (3, 'Facebook', 500000, '123456789', 'San Francisco');
insert into Donors values (4, 'Apple', 200000, '123456789', 'San Francisco');
insert into Donors values (5, 'LinkedIn', 3000000, '123456789', 'San Francisco');
insert into Donors values (6, 'Amazon', 1000000, '123456789', 'Seattle');
insert into Donors values (7, 'Oracle', 5000000, '123456789', 'Santa Clara');

insert into Advertise values (1, 'poster');
insert into Advertise values (2, 'placard');
insert into Advertise values (3, 'website');
insert into Advertise values (4, 'others');

insert into Working values (1, 1);
insert into Working values (1, 3);
insert into Working values (1, 4);
insert into Working values (2, 5);
insert into Working values (2, 6);
insert into Working values (2, 8);
insert into Working values (3, 9);
insert into Working values (3, 10);
insert into Working values (3, 11);
insert into Working values (4, 1);
insert into Working values (4, 3);
insert into Working values (4, 2);
insert into Working values (5, 1);
insert into Working values (5, 3);
insert into Working values (5, 5);
insert into Working values (6, 7);
insert into Working values (6, 8);
insert into Working values (6, 3);
insert into Working values (7, 5);
insert into Working values (7, 9);
insert into Working values (7, 11);
insert into Working values (8, 2);
insert into Working values (8, 4);
insert into Working values (8, 9);

insert into Funding values (1, 1, 1000);
insert into Funding values (1, 2, 1000);
insert into Funding values (2, 1, 1000);
insert into Funding values (2, 3, 1000);
insert into Funding values (3, 2, 1000);
insert into Funding values (3, 3, 1000);
insert into Funding values (4, 4, 1000);
insert into Funding values (4, 5, 1000);
insert into Funding values (5, 1, 1000);
insert into Funding values (5, 4, 1000);
insert into Funding values (6, 5, 1000);
insert into Funding values (6, 6, 1000);
insert into Funding values (7, 2, 1000);
insert into Funding values (7, 3, 1000);
insert into Funding values (8, 4, 1000);
insert into Funding values (8, 5, 1000);
insert into Funding values (8, 7, 1000);

insert into Adopt values (1, 1);
insert into Adopt values (1, 2);
insert into Adopt values (2, 3);
insert into Adopt values (2, 4);
insert into Adopt values (2, 1);
insert into Adopt values (3, 1);
insert into Adopt values (3, 2);
insert into Adopt values (3, 3);
insert into Adopt values (4, 2);
insert into Adopt values (4, 3);
insert into Adopt values (4, 4);
insert into Adopt values (5, 1);
insert into Adopt values (5, 3);
insert into Adopt values (5, 4);
insert into Adopt values (6, 1);
insert into Adopt values (6, 3);
insert into Adopt values (6, 4);
insert into Adopt values (7, 1);
insert into Adopt values (7, 2);
insert into Adopt values (7, 3);
insert into Adopt values (8, 1);
insert into Adopt values (8, 2);
insert into Adopt values (8, 4);
