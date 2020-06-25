const crypto = require('crypto');
const connection = require('../database/connection');

module.exports = {
  async index(request, response) {
    const cat = await connection('category').select('*');
  
    return response.json(cat);
  },

  async create(request, response) {
    const { name, image } = request.body;

    const id = crypto.randomBytes(4).toString('HEX');
    
    await connection('cat').insert({
      id,
      name,
      image
    })

    return response.json({ id });
  }
}