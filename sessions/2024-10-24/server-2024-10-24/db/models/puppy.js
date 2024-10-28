"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class Puppy extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      Puppy.belongsTo(models.Owner, {
        foreignKey: "ownerId",
      });
    }
  }
  Puppy.init(
    {
      name: DataTypes.STRING,
      ownerId: DataTypes.INTEGER,
    },
    {
      sequelize,
      modelName: "Puppy",
    },
  );
  return Puppy;
};
