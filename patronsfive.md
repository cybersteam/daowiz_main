---
layout: page
title: The fiver
permalink: /fivedollarpatron/
---
<strong>5$ per month patronage.</strong>
<div id="paypal-button-container-P-8AG245328G818664YMDKMQRA" style="border-radius: 25px;
                            border: 2px solid #73AD21;
                            padding: 20px;
                            width: 80vw;
                            height: 200px;"></div>
<script src="https://www.paypal.com/sdk/js?client-id=AWUGJ1f2zd3MOq6tljQpNyx7U7oGNSR8aYAeJiAFnvfanpPVWOuCTYsdXlnBKVsDV4ArMGSlcNRjQoqJ&vault=true&intent=subscription" data-sdk-integration-source="button-factory"></script>
<script>
paypal.Buttons({
    style: {
        shape: 'pill',
        color: 'silver',
        layout: 'vertical',
        label: 'subscribe'
    },
    createSubscription: function(data, actions) {
      return actions.subscription.create({
        /* Creates the subscription */
        plan_id: 'P-8AG245328G818664YMDKMQRA'
      });
    },
    onApprove: function(data, actions) {
      alert(data.subscriptionID); // You can add optional success message for the subscriber here
    }
}).render('#paypal-button-container-P-8AG245328G818664YMDKMQRA'); // Renders the PayPal button
</script>
<br>
<br>
<br>
