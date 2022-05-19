/*let building1 = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
let building2 = {
    numberOfFloors : 6,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 10,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
console.log('This building has '+building.numberOfFloors+ ' floors');
console.log('There\'s a total of '+(building.numberOfAptByFloor['firstFloor'] + 
building.numberOfAptByFloor['thirdFloor'])+ ' apartments on the 1st and 3rd floor');

console.log('The name of the second tenant is '+ 
building.nameOfTenants[1]);
console.log('The number of rooms in Dan\'s apartment: '+
building.numberOfRoomsAndRent['dan'][0]);

function build(b){
    console.log('This building has '+b.numberOfFloors+ ' floors');
    console.log('There\'s a total of '+(b.numberOfAptByFloor['firstFloor'] + 
    b.numberOfAptByFloor['thirdFloor'])+ ' apartments on the 1st and 3rd floor');

    console.log('The name of the second tenant is '+ 
    b.nameOfTenants[1]);
    console.log('The number of rooms in Dan\'s apartment: '+
    b.numberOfRoomsAndRent['dan'][0]);
}
build(building1)
build(building2)

let sum_rents = building.numberOfRoomsAndRent['sarah'][1] + 
building.numberOfRoomsAndRent['david'][1]

if(sum_rents > building.numberOfRoomsAndRent['dan'][1]){
    building.numberOfRoomsAndRent['dan'][1] = 1200
}
console.log(building);

//Exercise 5
let family = {mother:'Alice', dog:'Ghost', brother:'Armel'}
for(let item in family){
    console.log(item);
}
for(let item in family){
    console.log(family[item]);
}

//Exercise 7
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort()
console.log(names)































names.forEach(name => {society_name+=name[0]})
console.log(society_name);
*/

//Exercise function

function display_age(myAge){
    let mum_age = myAge*2
    let dad_age = mum_age*1.2
    console.log('I am '+myAge+ '\n My mum is '+(myAge*2)+' and my dad is '+dad_age);
    return 10
}

display_age(10)

function display_age(myAge){
    let mum_age = myAge*2
    return mum_age
}
display_age(10)
console.log(display_age(14));

let display_age1 = myAge => {return myAge*2}

function sum(num1, num2, num3){
    console.log(num1+num2+num3);
}
function is_even(num){
    if(num%2 == 0){
        return num+ ' is even'
    }
}


function is_prime(number){
    let m = Math.sqrt(number)
    for(let i=2; i <= m; i++){
        if(number % i == 0){
            return false;
        }
        else{
            return 'is prime'
        }
    }
}

















