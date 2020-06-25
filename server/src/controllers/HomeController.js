const connection = require('../database/connection');

module.exports = {
    async index(request, response) {
        return response.json([
            'Olá',
            'mundo'
        ]);
    },
};