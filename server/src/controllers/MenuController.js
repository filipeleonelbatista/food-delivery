const crypto = require('crypto');
const connection = require('../database/connection');
const db = require('../database/db');

module.exports = {
    async index(request, response) {
        let prod = await connection('products').select('*');
        let cat = await connection('category').select('*');
        let opt = await connection('optional').select('*');
        
        
        return response.json(opt);
    }
}