const crypto = require('crypto');
const connection = require('../database/connection');

module.exports = {
  async index(request, response) {
    const paymentMethod = await connection('paymentMethod').select('*');
  
    return response.json(paymentMethod);
  },

  async create(request, response) {
    const { name, image } = request.body;

    const id = crypto.randomBytes(4).toString('HEX');
    
    await connection('paymentMethod').insert({
      id,
      name,
      image
    })

    return response.json({ id });
  }
}