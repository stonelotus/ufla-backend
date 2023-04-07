const router = require('express').Router();
const actionHandler = require('./action.handlers');

router.post('/process', actionHandler.processAction);

module.exports = router;