class GDAXConst():

    '''
        Constants used for communication with the GDAX API.

        Request and result literals can be found in the base class GDAXConst.
        URL's for the live exchange can be found in GDAXConst.Live
        URL's for the Sandbox exchange can be found in GDAXConst.Sandbox
        Status codes can be found in GDAXConst.Status
    '''
    account_address = 'account_address'
    account_name = 'account_name'
    account_number = 'account_number'
    accounts = 'accounts'
    activate = 'activate'
    allow_buy = 'allow_buy'
    allow_deposit = 'allow_deposit'
    allow_sell = 'allow_sell'
    allow_withdraw = 'allow_withdraw'
    amount = 'amount'
    application_json = 'application/json'
    asks = 'asks'
    available = 'available'
    balance = 'balance'
    bank_address = 'bank_address'
    bank_country = 'bank_country'
    bank_country_name = 'bank_country_name'
    bank_name = 'bank_name'
    base_balance = 'base_balance'
    base_currency = 'base_currency'
    base_funding = 'base_funding'
    base_max_size = 'base_max_size'
    base_min_size = 'base_min_size'
    bch_usd = 'BCH-USD'
    best_ask = 'best_ask'
    best_bid = 'best_bid'
    bids = 'bids'
    book = 'book'
    btc = 'BTC'
    btc_usd = 'BTC-USD'
    buy = 'buy'
    call_funds = 'call_funds'
    call_price = 'call_price'
    call_side = 'call_side'
    call_size = 'call_size'
    cancel_both = 'cb'
    cancel_newest = 'cn'
    cancel_oldest = 'co'
    candles = 'candles'
    cb_access_key = 'CB-ACCESS-KEY'
    cb_access_passphrase = 'CB-ACCESS-PASSPHRASE'
    cb_access_sign = 'CB-ACCESS-SIGN'
    cb_access_timestamp = 'CB-ACCESS-TIMESTAMP'
    change = 'change'
    changes = 'changes'
    channels = 'channels'
    code = 'code'
    coinbase_accounts = 'coinbase_accounts'
    coinbase_account_id = 'coinbase_account_id'
    complement = 'complement'
    completed_at = 'completed_at'
    content_type = 'Content-Type'
    covered = 'covered'
    created_at = 'created_at'
    crypto_address = 'crypto_address'
    currency = 'currency'
    decrease_and_cancel = 'dc'
    default_amount = 'default_amount'
    deposit = 'deposit'
    deposits = 'deposits'
    details = 'details'
    done = 'done'
    done_at = 'done_at'
    done_reason = 'done_reason'
    end_date = 'end_date'
    entry = 'entry'
    epoch = 'epoch'
    epoch_time = 'epoch_time'
    error = 'error'
    eth = 'ETH'
    eth_usd = 'ETH-USD'
    exchange_volume = 'exchange_volume'
    executed_value = 'executed_value'
    expires_at = 'expires_at'
    fee = 'fee'
    fiat = 'fiat'
    file_url = 'file_url'
    fill_fees = 'fill_fees'
    filled_size = 'filled_size'
    full = 'full'
    funded_amount = 'funded_amount'
    funding = 'funding'
    funding_amount = 'funding_amount'
    funding_value = 'funding_value'
    funds = 'funds'
    heartbeat = 'heartbeat'
    high_24h = 'high_24h'
    high = 'high'
    hold = 'hold'
    holds = 'holds'
    iban = 'iban'
    id_ = 'id'
    instant_buy = 'instant_buy'
    iso = 'iso'
    key = 'key'
    l2update = 'l2update'
    last_match = 'last_match'
    last_size = 'last_size'
    last_trade_id = 'last_trade_id'
    ledger = 'ledger'
    level2 = 'level2'
    limit = 'limit'
    limits = 'limits'
    liquidity = 'liquidity'
    local_time = 'local_time'
    low_24h = 'low_24h'
    low = 'low'
    ltc = 'LTC'
    ltc_usd = 'LTC-USD'
    margin_call = 'margin_call'
    maker_order_id = 'maker_order_id'
    margin_account_id = 'margin_account_id'
    margin_product_id = 'margin_product_id'
    margin_profile_id = 'margin_profile_id'
    market = 'market'
    match = 'match'
    matches = 'matches'
    max_funding_value = 'max_funding_value'
    message = 'message'
    min_size = 'min_size'
    name = 'name'
    new_funds = 'new_funds'
    new_size = 'new_size'
    next_expire_time = 'next_expire_time'
    nonce = 'nonce'
    old_funds = 'old_funds'
    old_size = 'old_size'
    oldest_outstanding = 'oldest_outstanding'
    open_24h = 'open_24h'
    open_ = 'open'
    orders = 'orders'
    order_id = 'order_id'
    overdraft_enabled = 'overdraft_enabled'
    params = 'params'
    passphrase = 'passphrase'
    payment_method = 'payment-method'
    payment_methods = 'payment-methods'
    payment_method_id = 'payment_method_id'
    payout_at = 'payout_at'
    pending = 'pending'
    period_in_days = 'period_in_days'
    position = 'position'
    position_compliment = 'position_compliment'
    position_max_size = 'position_max_size'
    position_size = 'position_size'
    post_only = 'post_only'
    price = 'price'
    primary = 'primary'
    primary_buy = 'primary_buy'
    primary_sell = 'primary_sell'
    private = 'private'
    products = 'products'
    product_id = 'product_id'
    product_ids = 'product_ids'
    profile_id = 'profile_id'
    quote_balance = 'quote_balance'
    quote_currency = 'quote_currency'
    quote_funding = 'quote_funding'
    quote_increment = 'quote_increment'
    reason = 'reason'
    received = 'received'
    recorded_at = 'recorded_at'
    ref = 'ref'
    reference = 'reference'
    remaining = 'remaining'
    remaining_size = 'remaining_size'
    repaid_amount = 'repaid_amount'
    repaid_default = 'repaid_default'
    request_type = 'type'
    routing_number = 'routing_number'
    sell = 'sell'
    sepa_deposit_information = 'sepa_deposit_information'
    sequence = 'sequence'
    server_time = 'server_time'
    settled = 'settled'
    side = 'side'
    signature = 'signature'
    size = 'size'
    snapshot = 'snapshot'
    specified_funds = 'specified_funds'
    start_date = 'start_date'
    status = 'status'
    stop_price = 'stop_price'
    stop_type = 'stop_type'
    stp = 'stp'
    subscribe = 'subscribe'
    subscriptions = 'subscriptions'
    swift = 'swift'
    system_time = 'system_time'
    taker_fee_rate = 'taker_fee_rate'
    taker_order_id = 'taker_order_id'
    taker_profile_id = 'taker_profile_id'
    taker_user_id = 'taker_user_id'
    ticker = 'ticker'
    time = 'time'
    time_in_force = 'time_in_force'
    timestamp = 'timestamp'
    total = 'total'
    trade_id = 'trade_id'
    trades = 'trades'
    two_factor_code = 'two_factor_code'
    type_ = 'type'
    unsubscribe = 'unsubscribe'
    us = 'US'
    usd = 'USD'
    user_id = 'user_id'
    updated_at = 'updated_at'
    volume_24h = 'volume_24h'
    volume_30d = 'volume_30d'
    volume = 'volume'
    wallet = 'wallet'
    wire_deposit_information = 'wire_deposit_information'
    withdrawals = 'withdrawals'

    class Errors():
        amount_is_required = 'amount is required'
        amount_must_be_positive = 'amount must be a positive number'
        bad_request = 'BadRequest'
        cannot_deposit_less_than = 'cannot deposit less than'
        cb_access_key_required = 'CB-ACCESS-KEY header is required'
        does_not_exist = 'does not exist'
        does_not_match = 'does not match'
        insufficient_funds = 'Insufficient funds'
        invalid_api_key = 'Invalid API Key'
        invalid_level = 'Invalid level'
        invalid_order_id = 'Invalid order id'
        not_a_valid_product_id = 'not a valid product_id'
        not_a_valid_status = 'not a valid status'
        not_found = 'NotFound'
        price_required = 'price required'
        price_too_large = 'price too large'
        product_not_found = 'Product not found'
        size_too_large = 'size too large'
        size_required = 'size required'
        unsupported_currency = 'unsupported currency'
        unsupported_granularity = 'Unsupported granularity'

    class Live():
        rest_url = 'https://api.gdax.com'
        websocket_url = 'wss://ws-feed.gdax.com'

    class Pcts():
        b_pt_01 = 'b_0.01_pct'
        b_pt_05 = 'b_0.05_pct'
        b_pt_10 = 'b_0.10_pct'
        b_pt_50 = 'b_0.50_pct'
        b_1 = 'b_1.00_pct'
        b_2_pt_50 = 'b_2.50_pct'
        b_5 = 'b_5.00_pct'
        b_10 = 'b_10.0_pct'
        b_25 = 'b_25.0_pct'
        s_pt_01 = 's_0.01_pct'
        s_pt_05 = 's_0.05_pct'
        s_pt_10 = 's_0.10_pct'
        s_pt_50 = 's_0.50_pct'
        s_1 = 's_1.00_pct'
        s_2_pt_50 = 's_2.50_pct'
        s_5 = 's_5.00_pct'
        s_10 = 's_10.0_pct'
        s_25 = 's_25.0_pct'

        b_1 = 'b_0.01_pct'
        b_2 = 'b_0.05_pct'
        b_3 = 'b_0.10_pct'
        b_4 = 'b_0.50_pct'
        b_5 = 'b_1.00_pct'
        b_6 = 'b_2.50_pct'
        b_7 = 'b_5.00_pct'
        b_8 = 'b_10.0_pct'
        b_9 = 'b_25.0_pct'
        s_1 = 's_0.01_pct'
        s_2 = 's_0.05_pct'
        s_3 = 's_0.10_pct'
        s_4 = 's_0.50_pct'
        s_5 = 's_1.00_pct'
        s_6 = 's_2.50_pct'
        s_7 = 's_5.00_pct'
        s_8 = 's_10.0_pct'
        s_9 = 's_25.0_pct'

    class Sandbox():
        fix_api_url = 'tcp+ssl://fix-public.sandbox.gdax.com:4198'
        rest_url = 'https://api-public.sandbox.gdax.com'
        site_url = 'https://public.sandbox.gdax.com'
        websocket_url = 'wss://ws-feed-public.sandbox.gdax.com'

    class Status():
        bad_request = 400
        forbidden = 403
        internal_server_error = 500
        not_found = 404
        success = 200
        too_many_requests = 429
        unauthorized = 401
