module.exports = {
  env: {
    node: true,
    es2022: true
  },
  extends: ["eslint:recommended"],
  parserOptions: {
    ecmaVersion: 2022,
    sourceType: "module"
  },
  rules: {
    "no-unused-vars": "error",
    "no-console": "off",
    "semi": ["error", "always"],
    "quotes": ["error", "double"]
  }
};