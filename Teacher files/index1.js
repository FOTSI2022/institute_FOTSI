//Exercise 5
function changeEnough(itemPrice, amountOfChange){
    let sum = 0
    //amountOfChange =[25, 20, 5, 0]
    let real_value = [0.25, 0.10, 0.05, 0.01]
    for(let i in amountOfChange){
        sum += (Number(amountOfChange[i]) * Number(real_value[i]))
        //First loop : i=25; sum = 0 + 25 | Second loop: i=20, sum = 25 + 20 =45

    }
    console.log('Sum is '+ sum);
    if(sum >= itemPrice){
        return true
    }
    else{
        return false
    }
}

changeEnough(14.11, [2,100,0,0])
changeEnough(0.75, [0,0,20,5])

//Exercise 6

function hotelCost(){
    let nights;
    do{
        nights = Number(prompt('Hey how many nights would you like to stay ?'))
    }
    while( nights =='' ||null|| undefined || isNaN(nights))

    let costPerNight = 140
    let total_price = nights * costPerNight
    return total_price
}

function planeRideCost(){
    let destination;
    do{
        destination = prompt('Whats your destination ?')
    }
    while( destination =='' ||null|| undefined || !isNaN(destination))
    /*if(destination == 'London'){
        return 183
    }else if (destination == 'Paris'){
        return 220
    }else {
        return 300
    }*/
    switch(destination){
        case 'London':
            return 183;
        case 'Paris':
            return 220;
        default:
            return 300;
    }
        
}

function rentalCarCost(){
    let car_rent;
    do{
        car_rent = Number(prompt('number of Days you want to rent the car ?'))
    }
    while( car_rent =='' ||null|| undefined || isNaN(car_rent))
    let costPerday = 40
    if(car_rent > 10){
        let discount = (car_rent * costPerday)*5/100
        let total_car_price = (car_rent * costPerday) - discount
        return total_car_price
    }else{
        let total_car_price = car_rent * costPerday
        return total_car_price
    }
}
let totalVacationCost =() => {
    return hotelCost() + planeRideCost() + rentalCarCost()
}

console.log(`The total cost of your vaction is ${totalVacationCost()} $`);

let name = 'Jane'
let country = 'Cameroun'
console.log(`Hey my name is ${name} and live in ${country}`);


if(false){console.log('ciao');}

else{
    let n= prompt()
    if n >
}