+flag (F): team(100)
  <-
  .wait(2000);
  .wait(2000);
  .get_backups;
  .get_fieldops;
  .get_medics;

  .register_service("general");
  .wait(2000);

  ?myBackups(B);
  ?myMedics(M); 
  ?myFieldops(O);
  .wait(2000);
  +aformar;
  .print("Soldiers: ", B);
  .send(B, tell, a_formar([50,0,50]));
  .send(M, tell, a_formar([20,0,20]));  
  .send(O, tell, a_formar([20,0,20]));

  .goto([10,0,10]);
  .print("He llegado!");

  .wait(20000);

  -aformar;
  +acapturar;
  .send(B, tell, a_capturar);
  .send(M, tell, a_capturar);
  .send(O, tell, a_capturar);
  .goto(F).


+flag_taken: team(100)
  <-
  .print("flag_taken");
  ?base(Base);
  -acapturar;
  +returning;
  ?flag(F);
  .look_at(F);
  .goto(Base).

+myBackups(B): team(100)
  <- 
    .print("myBackups").


+myMedics(M): team(100)
    <- 
    .print("myMedics").


+myFieldops(O): team(100)
    <- 
    .print("myFieldops").

    