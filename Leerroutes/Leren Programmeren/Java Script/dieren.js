
function bereken_poten(aantal_giraffen, aantal_struisvogels, aantal_zebras) {
    const poten_giraffe = 4;
    const poten_struisvogel = 2;
    const poten_zebra = 4;
    
    const totaal_poten = (aantal_giraffen * poten_giraffe) + (aantal_struisvogels * poten_struisvogel) + (aantal_zebras * poten_zebra);
    return totaal_poten;
  }
  
  const totaal_poten = bereken_poten(5,5,5);
  console.log(`Het totale aantal poten is ${totaal_poten}`);