const router = require('express').Router();
const flowHandler = require('./flow.handlers');

router.post('/finish', flowHandler.finishFlow);

module.exports = router;