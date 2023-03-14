bird =[{'name': "mus",'key':'m','count':0},
        {'name': "koolmees",'key':'k','count':0},
        {'name': "kraai",'key':'kr','count':0},
    ]
totaal_aantal_vogels = 0 

function get_bird_by_key(bird, key) {
    for (soort of bird) {
        if (soort["key"] == key) {
            soort["count"] += 1;
            totaal_aantal_vogels +=1;
            return soort;
          }
        }
      }

while (true) {
    soort = prompt("Welke soort?");
    if (soort == ".") {
        break;
        }
        get_bird_by_key(bird, soort);
    }

function get_bird_percentage(bird) {
        let result = {};
        for (soort of bird) {
            let percentage = (soort["count"] / totalBirds) * 100;
            result[soort["name"]] = percentage;
        }
        return result;
      }

console.log(bird)
