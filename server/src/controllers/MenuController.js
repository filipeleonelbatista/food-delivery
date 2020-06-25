const crypto = require('crypto');
const connection = require('../database/connection');
const db = require('../database/db');

module.exports = {
    async index(request, response) {
        const prod = await connection('products').select('*');
        const cat = await connection('category').select('*');
        const opt = await connection('optional').select('*');
        
        return response.json(opt);
    }
}