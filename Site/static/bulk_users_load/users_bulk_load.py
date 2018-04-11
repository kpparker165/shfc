import sys
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

#  Update the users in this list.
#  Each tuple represents the username, password, and email of a user.
users = [
  ('user_1', 'user_1@example.com', 'Jason', 'Dumbass'),
  ('user_2', 'user_2@example.com', 'suky', 'mcsuck'),
  ('191215','david.j.achammer@lmco.com',' David J.','Achammer'),
('191582','michael.d.adamo@lmco.com','Michael D.','Adamo'),
('100002','john.r.adamoli.jr@lmco.com','John','Adamoli'),
('100004','curt.s.adams@ulalaunch.com','Curt','Adams'),
('100005','wes.adams@lmco.com','Wesley','Adams'),
('100006','Aprilndwayne@aol.com','Dwayne (Gene)','Adamson'),
('100009','gijams1@gmail.com','John P.','Affatica'),
('100010','kurt.ahle@dcma.mil','Kurt','Ahle'),
('100013','douglas.j.albrecht@lmco.com','Douglas','Albrecht'),
('191415','lucas.h.alexander@lmco.com','Lucas','Alexander'),
('100015','clayton.r.allen@lmco.com','Clayton','Allen'),
('191322','grant.allen@lmco.com','Grant','Allen'),
('100017','rob.allison@lmco.com','Robert','Allison'),
('191323','kelly.m.allred@lmco.com','Kelly M.','Allred'),
('100018','craig.s.altonen@lmco.com','Craig S.','Altonen'),
('100019','daniel.e.amerman@lmco.com','Daniel','Amerman'),
('100020','michael.c.amerman@lmco.com','Michael','Amerman'),
('100021','robert.andereck@lmco.com','Robert E','Andereck'),
('100023','eric.p.anderson1@lmco.com','Eric P.','Anderson'),
('191557','philip.s.anderson@lmco.com','Philip S.','Anderson'),
('100025','scott.d.anderson@lmco.com','Scott D.','Anderson'),
('100026','timothy.g.anderson@ulalaunch.com','Tim','Anderson'),
('100027','joey.andrews@lmco.com','Joey','Andrews'),
('100028','carol.j.angel@lmco.com','Carol J.','Angel'),
('100029','david.anselmi@lmco.com','David','Anselmi'),
('100030','RANSELMI@juno.com','Robert','Anselmi'),
('100031','michael.anthony@lmco.com','Michael','Anthony'),
('100032','roger.a.applegate@lmco.com','Roger A','Applegate'),
('191398','lee.arensdorf@lmco.com','Lee','Arensdorf'),
('100034','cindy.l.aris@ulalaunch.com','Cindy','Aris'),
('191547','david.s.armstrong@lmco.com','David S.','Armstrong'),
('100036','mitchel.c.arnold@ulalaunch.com','Mitch','Arnold'),
('100038','laurie.h.atkinson@lmco.com','Laurie H.','Atkinson'),
('100039','kurt.l.austad@ulalaunch.com','Kurt','Austad'),
('191317','Michael.Avant@dcma.mil','Michael','Avant'),
('100040','paul.s.avedissian@lmco.com','Paul S.','Avedissian'),
('100041','bryan.bachman@lmco.com','Bryan','Bachman'),
('100042','david.r.badgett@ulalaunch.com','David R.','Badgett'),
('100043','john.p.bailey@lmco.com','John P.','Bailey'),
('100045','steve.d.bailey@lmco.com','Steve D.','Bailey'),
('100046','christina.d.bain@lmco.com','Christina D.','Bain'),
('191298','jeffrey.a.baker@lmco.com','Jeff','Baker'),
('100048','(no e-mail address)','Jim','Ball'),
('100050','jeffrey.j.bank@lmco.com','Jeffrey','Bank'),
('100051','brenda.banks@lmco.com','Brenda','Banks'),
('191257','keith.a.baranoff@lmco.com','Keith A.','Baranoff'),
('191226','thomas.c.barboa@lmco.com','Thomas C.','Barboa'),
('191596','lee.a.barker@lmco.com','Lee A.','Barker'),
('191239','timothy.d.barlow@lmco.com','Timothy D.','Barlow'),
('191416','christopher.1.barnes@lmco.com','Christopher 1','Barnes'),
('191448','edwin.m.barnes@lmco.com','Edwin M.','Barnes'),

]

for username, email, first_name, last_name in users:
  try:
    print 'Creating user {0}.'.format(username)
    password = last_name+username
    user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()

    assert authenticate(username=username, password=password)
    print 'User {0} successfully created.'.format(username)

  except:
    print 'There was a problem creating the user: {0}.  Error: {1}.'.format(username, sys.exc_info()[1])

