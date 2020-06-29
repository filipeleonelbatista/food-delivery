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
  },

  async show(request, response) {
    const prod = await connection('products').where({id: request.params.id}).select('*');
    const opt = await connection('optional').where({id_product: prod[0].id}).select('*');

    return response.json({prod, opt});
  },

}