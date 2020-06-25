const crypto = require('crypto');
const connection = require('../database/connection');

module.exports = {
  async index(request, response) {
    const optional = await connection('optional').select('*');
  
    return response.json(optional);
  },

  async create(request, response) {
    const { name, image } = request.body;

    const id = crypto.randomBytes(4).toString('HEX');
    
    await connection('optional').insert({
      id,
      name,
      image
    })

    return response.json({ id });
  }
}