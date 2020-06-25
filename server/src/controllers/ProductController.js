const crypto = require('crypto');
const connection = require('../database/connection');

module.exports = {
  async index(request, response) {
    const prod = await connection('products').select('*');
  
    return response.json(prod);
  },

  async create(request, response) {
    const { name, image } = request.body;

    const id = crypto.randomBytes(4).toString('HEX');
    
    await connection('products').insert({
      id,
      name,
      image
    })

    return response.json({ id });
  }
}