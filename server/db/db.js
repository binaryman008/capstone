const Sequelize = require('sequelize')
const db = new Sequelize(
  process.env.DATABASE_URL || 'postgresql://akshay:123456@localhost:5432/akshay', {
    logging: false
  }
)
module.exports = db
