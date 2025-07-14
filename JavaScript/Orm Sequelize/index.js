const sequelize = require( "./module")
const Customer  = require("./Customer")
const Order = require("./Order")

Customer.hasMany(Order) // Define a one to may relation between customer and order

let customerID = null

sequelize
    .sync({force: true}).then(result => {
       return Customer.create({name:"Benoit", email:"benoit@gmail.com"})
    })
    
    .then(customer => {
        customerID = customer.id
        console.log(customer)
        return customer.createOrder({total:45})
    })

    .then(order =>{
        console.log(order)
        return Order.findAll({where: customerID})
    }) 

    .then(result => {
        console.log(result)
    })

    .catch(err => {
        console.log(err)
    })