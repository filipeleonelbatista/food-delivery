const sqlite3 = require('sqlite3').verbose()

const db = new sqlite3.Database("./src/database/db.sqlite")

module.exports = db
db.serialize(() => {

    console.log("\n\nMaybe you will need delete the file db.sqlite manualy\n\n")


    // ####################################################
    // #                                                  #
    // #                                                  #
    // #                  TABLE CREATION                  #
    // #                                                  #
    // #                                                  #
    // ####################################################
    db.run(`
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image TEXT,
            name TEXT
        );
    `)

    db.run(`
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image TEXT,
            name TEXT,
            description TEXT,
            value TEXT,
            id_category INTEGER,
            FOREIGN KEY (id_category)
               REFERENCES products (id) 
        );
    `)

    db.run(`
        CREATE TABLE IF NOT EXISTS optional (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            value TEXT,
            id_product INTEGER,
            FOREIGN KEY (id_product)
               REFERENCES category (id)
        );
    `)

    db.run(`
        CREATE TABLE IF NOT EXISTS address (
            id INTEGER PRIMARY KEY AUTOINCREMENT,            
            street TEXT,
            number TEXT,
            district TEXT,
            city TEXT,
            state TEXT,
            contry TEXT,
            notice TEXT
        );
    `)

    db.run(`
        CREATE TABLE IF NOT EXISTS client (
            id INTEGER PRIMARY KEY AUTOINCREMENT,            
            image TEXT,
            name TEXT,
            email TEXT,
            mobilePhone TEXT,
            otherPhone TEXT,
            id_address INTEGER,
            id_paymentMethodPrefered INTEGER,
            FOREIGN KEY (id_paymentMethodPrefered)
               REFERENCES paymentMethod (id)
        );
    `)

    db.run(`
        CREATE TABLE IF NOT EXISTS paymentMethod (            
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image TEXT,
            name TEXT
        );
    `)

    db.run(`
        CREATE TABLE IF NOT EXISTS request (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_client INTEGER,
            totalPrice TEXT,
            discount TEXT,
            notice TEXT,
            id_paymentMethod INTEGER,
            FOREIGN KEY (id_paymentMethod)
               REFERENCES paymentMethod (id)
        );
    `)

    db.run(`
        CREATE TABLE IF NOT EXISTS requestItem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_request INTEGER,
            id_product INTEGER,
            id_optional INTEGER,
            notice TEXT
        );
    `)
    


    // ####################################################
    // #                                                  #
    // #                                                  #
    // #               DEFAULT INFORMATION                #
    // #                                                  #
    // #                                                  #
    // ####################################################



    let query = '';
    let values = [];

    query = `
        INSERT INTO category (
            image,
            name 
        ) VALUES (?, ?);`;

    values = [
        "https://images.unsplash.com/photo-1490645935967-10de6ba17061?ixlib=rb-1.2.1&auto=format&fit=crop&w=1035&q=80",
        "Todos os pratos"
    ];

    db.run(query, values, function (err) {
        if (err) {
            return console.log(err)
        }

        console.log("Success added")
        console.log(this)
    })

    query = `
        INSERT INTO paymentMethod (
            image,
            name 
        ) VALUES (?, ?);`;

    values = [
        "https://images.vexels.com/media/users/3/143188/isolated/preview/5f44f3160a09b51b4fa4634ecdff62dd---cone-de-dinheiro-by-vexels.png",
        "Dinheiro"
    ];

    db.run(query, values, function (err) {
        if (err) {
            return console.log(err)
        }

        console.log("Success added")
        console.log(this)
    })

    query = `
        INSERT INTO paymentMethod (
            image,
            name 
        ) VALUES (?, ?);`;

    values = [
        "https://image.flaticon.com/icons/png/512/147/147258.png",
        "Cartão de crédito"
    ];

    db.run(query, values, function (err) {
        if (err) {
            return console.log(err)
        }

        console.log("Success added")
        console.log(this)
    })

    query = `
        INSERT INTO paymentMethod (
            image,
            name 
        ) VALUES (?, ?);`;

    values = [
        "https://image.flaticon.com/icons/png/512/147/147258.png",
        "Cartão de débito"
    ];

    db.run(query, values, function (err) {
        if (err) {
            return console.log(err)
        }

        console.log("Success added")
        console.log(this)
    })
    

    // ####################################################
    // #                                                  #
    // #                                                  #
    // #                  TEST INFORMATION                #
    // #                                                  #
    // #                                                  #
    // ####################################################

    query = `
    INSERT INTO products (
        image,
        name,
        description,
        value,
        id_category
    ) VALUES (?, ?, ?, ?, ?);`;

    values = [
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1202&q=80",
        "Hamburger delicioso",
        "Hamburger delicioso com pão, hamburger de 150g, queijo, alface, tomate, cebola.",
        "19,90",
        1,
    ];

    db.run(query, values, function (err) {
        if (err) {
            return console.log(err)
        }

        console.log("Success added")
        console.log(this)
    })
    query = `
    INSERT INTO optional (
        name,
        description,
        value,
        id_product
    ) VALUES (?, ?, ?, ?);`;

    values = [
        "Hamburger adicional",
        "Hamburger de 150g.",
        "3,90",
        1
    ];

    db.run(query, values, function (err) {
        if (err) {
            return console.log(err)
        }

        console.log("Success added")
        console.log(this)
    })

    query = `
    INSERT INTO optional (
        name,
        description,
        value,
        id_product
    ) VALUES (?, ?, ?, ?);`;

    values = [
        "Queijo",
        "Queijo.",
        "1,90",
        1
    ];

    db.run(query, values, function (err) {
        if (err) {
            return console.log(err)
        }

        console.log("Success added")
        console.log(this)
    })

    query = `
    INSERT INTO optional (
        name,
        description,
        value,
        id_product
    ) VALUES (?, ?, ?, ?);`;

    values = [
        "Alface",
        "Alface.",
        "0,90",
        1
    ];

    db.run(query, values, function (err) {
        if (err) {
            return console.log(err)
        }

        console.log("Success added")
        console.log(this)
    })

    query = `
    INSERT INTO optional (
        name,
        description,
        value,
        id_product
    ) VALUES (?, ?, ?, ?);`;

    values = [
        "Cebola",
        "Cebola.",
        "2,90",
        1
    ];

    db.run(query, values, function (err) {
        if (err) {
            return console.log(err)
        }

        console.log("Success added")
        console.log(this)
    })

    
    // Fim da criação
});

