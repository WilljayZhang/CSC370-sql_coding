/* 1. How many volunteers does this company have? */
create view P1 as
select count(*) Number
from Participator
where Type = 'volunteer';

/* 2. How many activities does everybody participate in? */
create view P2 as
select Participator.Name, count(*) Number
from Participator, Working
  where Participator.ID = Working.Participator_ID
  group by Participator.ID;

/* 3. How much does Oracle donate? */
create view P3 as
select Funding
from Donors
  where Name = 'Oracle';

/* 4. Which campaign was held on 2019-6-1? */
create view P4 as
select ID
from Campaign
where Campaign.start_time = '2019-6-1';


/* 5. Which campaigns was finished on 2019-3-30? */
create view P5 as
  select ID
  from Campaign
  where end_time = '2019-3-30';


/* 6. Which campaign uses the least types of advertise? */
create view P6 as
select  Campaign.Content
from Campaign
where Campaign.ID in (
select Campaign_ID
  from Adopt
group by Adopt.Campaign_ID
order by count(*) asc)
limit 1;

/* 7. Which campaign has the most workers? */
create view P7 as
select Campaign.Content
from Campaign right join Working W on Campaign.ID = W.Campaign_ID
group by W.Campaign_ID, Campaign.Content
order by count(*) desc
limit 1;

/* 8. How much have each donor remained? */
create view P8 as
select D.Name, D.Funding - sum(Funding.expense) Remain
from Funding join Donors D on Funding.Donors_ID = D.ID
group by Donors_ID, D.Name, D.Funding;


/* 9. Who have participated the campaign in New York? */
create view P9 as
select Participator.Name
from Participator
where Participator.ID in (
  select Participator_ID
  from Working join Campaign C on Working.Campaign_ID = C.ID
  where C.Address = 'New York'
);


/* 10. Which donor have donated the campaign in Washington? */
create view P10 as
select Donors.Name
from Donors
where Donors.ID in(
  select Donors_ID
  from Funding join Campaign C on Funding.Campaign_ID = C.ID
  where C.Address = 'Washington'
);
