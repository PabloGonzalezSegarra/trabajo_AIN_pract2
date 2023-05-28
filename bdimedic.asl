//TEAM_AXIS

+flag (F): team(200) 
  <-
  .create_control_points(F,25,3,C);
  +control_points(C);
  .length(C,L);
  +total_control_points(L);
  +patrolling;
  +patroll_point(0).
  //.print("Got control points").


+target_reached(T): patrolling & team(200) 
  <-
  //.print("MEDPACK!");
  .cure;
  ?patroll_point(P);
  -+patroll_point(P+1);
  -target_reached(T).

+patroll_point(P): total_control_points(T) & P<T 
  <-
  ?control_points(C);
  .nth(P,C,A);
  .goto(A).

+patroll_point(P): total_control_points(T) & P==T
  <-
  -patroll_point(P);
  +patroll_point(0).


//TEAM_ALLIED 

+flag (F): team(100) 
  <-
  .register_service("medic");
  +start.

+a_formar(Pos)[source(A)]
  <-
  .print("A formar!");
  +aformar;
  .calculateFormation(Pos, X);
  .print("Pos: ", X);
  .goto(X).

+a_capturar[source(A)]
  <-
  .print("A capturar!");
  -aformar;
  +acapturar;
  ?flag(F);
  .calculateDest(F, XF);
  .goto(XF).
  
+flag_taken: team(100)
  <-
  .print("flag_taken");
  ?base(Base);
  -acapturar;
  +returning;
  ?flag(F);
  .look_at(F);
  .goto(Base).

+enemies_in_fov(ID,Type,Angle,Distance,Health,Position)
  <-
  .shoot(3,Position).