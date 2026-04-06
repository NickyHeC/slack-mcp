Source: https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks

# Sending messages using incoming webhooks

Incoming webhooks are a way to post messages from apps into Slack. Creating an incoming webhook gives you a unique URL to which you send a [JSON](https://en.wikipedia.org/wiki/JSON) payload with the message text and some options. You can use all the usual [formatting](/messaging/formatting-message-text) and [layout blocks](/messaging#complex_layouts) with incoming webhooks to make the messages stand out.

If you're looking for the Help Center article on using webhooks with Workflow Builder, [head over here](https://slack.com/help/articles/360041352714). Otherwise, read on!

* * *

## Getting started with incoming webhooks {#getting_started}

We're going to walk through a 4-step process (if you've already done some of these things it'll be even easier) that will have you posting messages using incoming webhooks in just a few minutes:

### 1. Create a Slack app (if you don't have one already) {#create-app}

[Create an app](https://api.slack.com/apps?new_app=1)

Pick a name, choose a workspace to associate your app with (bear in mind you'll probably be posting lots of test messages, so you may want to create a channel for sandbox use), then click **Create App**. If you've already created an app, you can use that one. Have a treat for being prepared! 🍪

### 2. Enable incoming webhooks {#enable_webhooks}

You'll be redirected to the settings page for your new app (if you're using an existing app, you can load its settings via your [app's management dashboard](https://api.slack.com/apps)).

From here, select **Incoming Webhooks**, and toggle **Activate Incoming Webhooks** to on. If you already have this activated, well, you deserve another treat! 🍪

### 3. Create an incoming webhook {#create_a_webhook}

Now that incoming webhooks are enabled, the settings page should refresh and some additional options will appear. One of those options is a very helpful button called **Add New Webhook to Workspace** — click it!

What this button does is trigger a shortcut version of the installation flow for Slack apps, one that is completely self-contained so that you don't have to actually build any code to generate an incoming webhook URL. We'll [show how you can generate webhooks programmatically later](#incoming_webhooks_programmatic), but for now, you'll see something like the following:

![Permissions screen with incoming webhooks channel selector](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAdAAAAGLCAMAAABAyjMGAAAAvVBMVEX////t7e3y8vLv7++1tbb/AHD8/P35+fkAjEzw8PAAeCtpx6cEBAYAgWQAqXcApnMluMswMTMVFhkiIyaam5wAhEDo6elvcHJfYGLh4uL+AFb19fU9PkD/AGaPkJHa2tpISUz/hbvy+vf/8/jExMWtra97e32jpKW7u7zMzM2EhIb/AHfT09RTVFYAkVYBs8U3vtAAmWKk2suF0LsAelt8w7HI594ksYoAaUcAaBT/0OT/Up7/sNJIuZb/Ko4qRI4jAAAACXBIWXMAAAsTAAALEwEAmpwYAAAfIUlEQVR42u2d+VfbSLq/n5JtyTt4wQsmmMWsQ27udJ/pvqdn+v7zd2bO7e5vb7czCQTCloDBGxhjY8m29P3BNpgOEOhAD6bf55wEWVUql/TRW/VWqawXBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQLlCPvobTd8q9dafcn68u35huD35wfhBB74G/3k2i6X/cIfPXrZvTf1oa/NR5WxdBP5nZ3dTBHbKnDibf3jrzTHFh7YbkhTWFcgaqshnbfPyCao+9gvMPmv0m1jSUo0ApBaA2nWFocjWEaww05+DggDNU1XaLctc1uFq/R3JQODgKsdAhZi3nqHPrdFDDUm8R9BoDZbNnoI6j1BA1uyLodR6RwyUfd1hs9I8s6HvFwg0eUb+17ba4SpyieyTVcXVcB7/p0Cw71w9EW5sLrF3jESlA9fQEhsUpGgpBU+EIztbYFSkfVXmlaNyQuuNyvbpS0txbBTjK6anqoJRY6L3pefDs7/C3vQ9Txr8dK35Ez1jpJvNVpuuN88F80cKa1hXTQTldK1XD4ugOhYXOHwJ/vyJh6yt1o5GuFGOvb3RQt5nCWf+1ka5pXctEnKKH4SR5Xco//2F0rj9uyeq8+tiAY3tbKdfawsKlIYvTG7Gcd6PDM24ZBgs9GMtfn7j131zX6i4pdzzV1btFPX+9lZquN/MX7e7CmtZrbxmQUslM0f3h8s9en9h2pa5JqbcLDbvT6XQ6Ha0WvslKp2Za6xdGmusZaN9K1fA0uMMybDnJ/uqh2OzF53/+98Y1T9haRO1q/5Hn6Ue60uneEGaBNdV1hVRXS+UMVZs7lJPzs6njvzr/PDfR3NbYlc1uPhGkXrhdkdtTyuV6tbDGGlqvcXV6fajqb4qgD6VnZoOj3LmR/pOv8v4rh6QF4nZ255aKMmXOrC9A5+25lv1uszdukT70/ri0uCe55Yq4NtIDvu7W+sw0V0w8FEqx5tJtv2N7W0231i4GKQrlODiO44BS0uTeq5/77CMaW3/nK3W1jRZu/zXbTLl8P89u9oYr6mL46Six0Ifjn5Odo870//v13oPwFe5u4W3lLkU7U9943zDb70RVz891lEwsPCT/MKaN76zb5TVt7jKTrz8LpWZ1ZnvLFMDpiSlN7kOyddXazvRm8dMvR3m/qdxjufXZzcEZP2d4BqLDYaHzh7/LqWR39mnitPgl8IaZrmE6AGp4THQoBO2M3mKx7fTGpxvojH9f0zRt3+VvLQy0u46sKbpn9j+e5au265MNVP3YbNoAzU3XT6XZtzOK8+egjjhFvytfVTsHn6on+syBho2taTRbvPS+YeaipZUm9x4Z/7ieR/fhETVtNNBA87LpCqUWgsziOEoNT6M7HE9bvv3qI/3nu5v11BcW9Nt4RPvn8xVNjebm/k/7s/qMGqq180MxbDkYu8k8ZtPahutm+7Ts2vTWxwauM9V9NLw00eyusE2a71qfObObjpJFYvdrolvT1/yq8Kv8+PEmH21u193ORxTNqh/HLc3WLPuyNzbzy38adCUdjkv1yOsXdZuncBpu/ccz/Uj/Uj+6nPy33dZxq9A4/xw02kdXlmM/O07XfrVaxTVG9cIjMry7Sm87DuBoDoCmHLSK7q6l9fAxKPxHYqH31eiCK/xXV9n7t0trxf620/mYcfb6TmvVzfS2eaNHBE2ta5+2pjfB1jTb1qxN5R5LObObSJN7nxRTR0e4OieDbe8t9Jzz9JcqNAxnau16j0gPHWADGrZmY1saNraXJqBc3l/+81/umbci6D0bKcyfmOdrFb5SOx/vPJ1Ob6G1yzBvGnnMVPdtNNvG1jTdwrY18DabGramwaa33PrTcCy1HrLJ+Tektop/3c/A3vi3Y7f4dcTG+daC6V+9wSOaAWzNBluzbDRsr9UENNvWsGhuqp9afz4WQR/CUFNb7EBn604vX9DDx5HVm+aINvE2sTVssNHQm00NNPQmoDfB6YxXN0XQh2p7U3ec58uYruv1BHd5H5qa3rTRsAG7a5q21uxPv9j2/lA0uUM6l3tHPXXTfYOe2R0XTU0DC9DRNA2auqaB1hXXsm2GZW3uH+MdC1a8vXrTHFF5m97kEJaOhQ1NTbds7fy273pMYqGPhdWNG+eIulpqoGk0Lb07drXQbLwAto2mDcm1kp/kZ9FntrW+IdpgY2ndZYU2NDUvthfbvpijkCb3sV+Cve5g07Y1DRsNy+7d6Zqt2bal2ZZma3S7WLHQR2+gO++8vQURXRdIxwZNu5g27PWuOvI89H6mEh4u+zbATGhfw7a7LWxPRi96b+zSVXmI7vs/9Ns4P+uA2ve0brPYYazI+J4IyuN+X+4Xbd4fjwGU4tflOU8pmeJvCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgCDdjuDK//eDMYppPjr6XuXjZre+K5MStC0ov9ktSi4mBXQnQc1n+EC9AXnoe9J1NLV51HSPL3Q137FKyMgY+2O8jl49ajo3EktlfZ7tCxIHXxrZGkr3KxMY+zOluJG97Mp73C/276v3IxS53IwkHV797VVf6kxJ08t2eO+qpvU9+eFquVqW7MWoORoFcGo3eUF5q1x2M1TsfywaBlYvtwli9e8scmE0+5XW8DT54L2+jX4J+dRRgOzP2lARdqASrh7uHtcn61BU3b+8SxC7tXVc3xNhZPPUe7r6JeT+SDbhkv288RR2It5qFD3OuW4fcOdpqbnDXunXIdbKNN/aekKCJ4uhBB7BeBfeXyKRhyX3tG7S7Sfo4KV8GYGlRARTILiYuTKQM7Gz0syUSKHcaWHH3+lptMQdgHBU17aJViJkp0JrxNui5xV5HujK3BKC3un18Og3g6v6f5SKnyupAIqtf1DRz6Sz6JQC5xGBlQDeVy2cAmVzOGH5BvdbBucFUsJsLyUI4MtdP7QfNsAFjIVYYiSxAtK6a/gDkYoViJElHj86fFtr9Y/wkdAC9l01puYjXQ3oiHzKTAJOjh0eRJZb8Z+ZIZOa8IhvBSoIxTJgLHRV9y4CR2i8VplIpYoGu2UVqaWDZygDhwZxztQ4wWutZZ2LicMRzNKhOOtA33Ikj10BlQC207bAvCfGzo6PAArAwsTTEglrnLdGB4aGjFUeCRjifPfcXVpaWlpayHsCqu3WXvpcl6HHiVZ2lg1C6MgY4JQaO2QzWA5Mr0M82YpVTmZbLJFhN1JdhsqJVK8Zh4k2ciWS1clGTIipdn8zjzrv1SnB3GbKnSX+w1ho9j97h0ILEnhmCpVZoIGfVsoGq1TfH48Sx223mrjjfqeNg/qIygN4KUTtRxJsplx7fW4DqcZHh5Xns/HaZiKCCSSAb7L2TPx2JRWKxWCwSi7q7QVH04CRMBgGmeh1rOjg/eAxMRoLBlOpnmw8uAPNBgLkomeAkQHQZIr9yXePRSERHj0wAJIOKWBKIxyDbPQgiz2FyYioFy1Gdfs4E81EXMB/1EQ+uMBdcBHLBXgCjeHCFbHCSTHSZVDB7UZleK5yMAb5oCuB5NEPanRliCy06/cuq1wM9T8XC3x+feMLpdDodDljTYGEkZglCUE9A5uTcU2peOobdo1TwNGt0s1HV1wDDmE8mky0rE9Gt+WQyaVU+jHZRCreSFrFWEyCEi5AFpO0B7zu9Z2Br3pZOXrfS/ZwjvzqnE33rynhUTiNlhXYuKhPpB93QIWOFACwrTL69N8SCRq1A3ytptUn9ukF2dl6+fPlyxwBIp8b0Gv1w2bbVvLbQjYPx0rOL8SZQs90jIyP+THEVh5GRkWjkiihIOmsQ6LrUHkZpEElO7cUGol851jMaatWZ1Vuhi5xHl2Iq1VDqmmAf1a7I/cq8vRRKxQXwlnWGO/bZEe1zxyd4OWj9wJYGrOR9B1H0YLe/Q9PNKwLdn4/tcHez9Qi1X/V8zIPk6+vu0yqpPHXOut3lMcWkg39noJvldcyaK+3gV7b+djAnRPf61ymE4+jWVdFuVOrVVMl3dlGZAZfPoQMwu7f4cri93Hy0NN/taeqBjRuD55TM9+2CxwLalgf2Mq0rJ1jicwCnrHWz9b/muDtU4cw4u3wD+H41VMh7agDHdEicHh++ujwZEKudjUEzn9LtwZxNyx4YgXasSUDxgVNUpqXHBirTv74WnOktgLqxfpeJxscYnXA3uR9JF/z28XQF6Flp31YtvX8lptejp4trrmgVqJDysXZiBWbcVtG/H7h0THorNYK+5T2lQspnr2MdA6WJg3hqNRX5Zc9tPj/zntTHVi1fY7HR6rT1g8t2HjuYcnsqp95TvPWAH8benQ3OXR2PgmYfpw8GcypcS+vxPQXQoRKpzLmO8hfB2jvnZ7O3sp06OK9Md3d4f6F8vDeXTwU5PW62md+fe+B21/WgpddnOGyfddKvahCCKvih2mu9tHq3Gzwt2afhE29ic9RXxJzPm+Fidfa0cVp3HcXUpWMKqbNG4zT1Dsz5vOmqZqxIDTDDnVOvx13Cnsmbp63YG0g0j9p+1eo0L4Jwq1OozJbNejv9DkZco0GNSvjUT7s3pVdKBN9AfUSV24M5q7br1OtU9VOemSMFJ+E+qbs8/rFua/3MHCmMdtqNMFqdQraSrZxXpnsX+YvaRLliu8xme7wAsVqoMuRPWxLZfiujGYCuGYMfAV3TgexKz8Uh2+2g0ivnuS+OQc+mz+PyDjxH0Vb6u9O9GZ3MChC/GLwY/YmjdBZgMZgASEYv6nHeTmYYzAkYKwoyer+MbBoyxkWxumb0d7gSlyoDsKINTEShJySY3W8nHT/ZuSZpZTvgePKz5eDuUztp1xMWNOS7tr8qzJx2dK359PR80hZ6MznlbNoIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIPJGXZvgsXa7Mo8bSz/i3RIUQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQhD8Etw43uUQmVL0yJR7OlH/r12fGg91C57TG1TnS3mD9dkUl3XWA3NXVTE+qgXKMmbFg9UkKesuF1ompd06pNpX9MEVFOp/w9eG9XlDl1hWlJBYMaDUj6AvpjxcVOYgAcNS8CLs9cNzIbuwi70qwVKilDHJz157wgvGUBdXatZTXH8VzxZlzdLD2m7/+pNmrQHPkw8RKwQRj4g1jpdjHi6rpH0QDHTyuPSBQJj/uryfCDrXWdaVVCuZTFjTB6cbe3sb2BrCU04EELOWAhDWWUT4DErCYzmRYWYK0uxvHWnUtOmvA0qIGqHT3PyNBYjED7LXzQHYxEwYgtwhoirRbgTGOUqq06uCzm6pXVrpX4cu1GMQGSLvToPvspjLAt7gEUPYt9iJgR8zSnrX6xsqoZsLXrTlk3d3UJbcGxjgJpT/ZPlRzRvqx3bOhI01r2WTGR+u1pKn5bTyj3kCN0GRkL+azE7XjiURbdaZKQLoxUYHJmkW2jDvQYP6kCfOdk5g/WWskCuAbmSwzf+x0TjglG6IdjFRnw+OO48+WIpaTHB31hZvzRU1FU5VEFeZOzz6sRbczHLV8FQCfq54ImdHmZHm6rKlwrBL3OEejp+Mn7md5J1sCKAYDVQB/u+2Ll2e8vlKskmzMHgcbZKaqo0yVIpbjyx48WQud0fs3a+YkUnUC3hXYquy7Ss+sQ6dlms1GCnabU7tOyZ2Plk9dDV8NIB8uAfWQ9azqKcabi1QBqnWKtULNWAdwIL4fLcQ10E7829v+Dt5SxWyMF4yyG9M0A430SQKvuamfAmce58Na9DpC5Zufn5+fVyP4nHAhWFSbCbydd4vNeNEzAkqV/JmCAeDESoFUDhyf0VmndtqOrc9bzV8yzhLR2vvtWjFbdtM59DxZQd3nW35Vsfd2PUWqoyW7EGzgBEby+VEFjO6+NB3jVWdD+XdMXyMDEGwtMefsZkvhgrk23SQGMBIAx9XOmwDKphPYsF66vcwqe2lp8zhRNlTePCPlGOTzeU2F9jTqecux5lhpqCtr0etFqycnJye42Tncsd6pWVujnjeb02tmYY2mUvm9M1IArIcmzYNlCm4n79DWSztGKZ1YKtNh73RlKeMEHIN8wXqyglasfsvscfYAw8dIz7wA2AbG2oCNAtsNmqoAvBw9ouXBa7SBzsU4YUyN9je3UJ3u71RNtEolFijrxMCj/AQBWtRooUMheEYpnL++Fo738ODg4MApQ2I+mYTucdW+/9wrFYD8q6PJ3ZXuz2PrUYiqilGxPXZWuYqVpm53v3sYcd8mU2Gi0Ns61QDGoPqx9qjrJPoqi4dhbGcf6A9W3fXePTD4m2MHGupN96ahA63B3r1bycjh4uHoTbU4H/nkytWw67B/XPkiebDUV1GzdzO04SAyugqwUvPuAAfwtMehoVYqAyQXW+YCpLdu3Rith97rO2wyB5lWmkJLRz8JDOaYJtSBhNXE4ywA2YuxUVvri+mcAa/19xOr3VvgxlqMUDYO192qd1y6noGsMSi9ex6YpEq7/wN2J3wKpNUbxwTSvu53P11BXzets+epWLud9xZTSSu4hjoDEmfQOIFpE967gSNzDFplODN7wz4PIejESqlkI/wWzQgkI3XAnO0mW+YRQTWRVHjJa8VUciJMywTcZgfNnErqbTNEhVZqCYL0JNz5oBZAyDrqTlGckLaWl0tsU6GVWtkYbSZTnRb9UoFcKZKaqmgFwqfPJ1EngHk2kUw1Z62UNZV83kygmVNJ9YRnitpHqSKB8galKCp+AKNx4HUctFGwoofEfUAq6gFvCMLR3ij/yLMBrI87yrVtUtB1FfUE8ER70znuaIqXoTaO14BS0lHaBvVoGarRMqvpUIeT6L8oJI3wKriN0151PqgF8K9o1/K9o7wKVigmMhSSRrhgvQ8ox2Uf90sFVo9DnD0rwcYkfrRRIO8NKye1wWu3rszwDqvpUEdeNPEhRmzy/gqLJOWC3peF/lam7M69lZXT5A0f9/i05behl07uzyHXDkUvQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEAQlmhwSzQ4LZCYIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgcH9LUB6e9MiGXPtbk6vmeSRvEruGOWdHZLo9ldG6/bjvuElZynQntMncI3l545Xoxy1bRLoLtjrWH7GgLiqi0d1o037Egpq0RKK7kcd4xIIKv8kKRFB5o7UgggoiqCCCCiLoHxX37ebSw2U4Hss/QAWW2usr5vqdD0sauyLeb7fQ8J7tOOFa8sr5p6X4VZu35axG6ezu9W5bot0nCGoz5j0KjdcjVyVW7Ks2b0s1iPc3tPs+R7T7pD7U3rN33gTriavS/Fdu3orEIu5slTSQm1Ogg57LAUYacr1HDEtuBSQyLOVAzy2Kanzq89DY6UgZ8LZjFRbdo/5UBUgHR7MjpzzT6jPaZAlIxHqbiUxo1N24tjTlO+vZlxor4+50zLFiYsxCzWn+00VLa4cjVXtk1Fdr5jw11FQ56pksEwqpiruZ6zTOYt46Ybv+R5Lp4pLdm4V21T9h+b3X7z6YhBXTDBcraXvkjIbVBvD1NlfaZb3ZnMp8vFS9kQ7s+GzPW5LV/W3XVqiy8t71/n37BM9ZPdRMbrkg266+HyvmcPbdzQ7Hqqk3xDX/VOaCbmAumCIXXAbmg0ukgoDPgKmp83xTU0AmEjFgJXhtLEEtfqFIapnJFBCLA7EsqQiZTDq4RDQOPJ8iF1wyMkykSEb7d0g8ChNPM1KhlslkMhktc9MluxcL1VOp57F8vMqp/grYpkKUOTgzrwoHXDPhZaD1cRPNJU3Xsu2eT5PsLCVSdpsxUtFovB+Otwgu/Wg++rweBf8eQHpyPvhUHaJ0ZKTRaDQaI2fLDzwOBXe7GHPWwe2tAFbCzVZuKxY7LnyYtUFmB+hYoY+X6msXHWvkJJ5/NVHzh052qBlVG+qvB240dQj+V70Py3nbG2ofPU1BO4FjA8CxCg8tqPW+fSnSeH2Es18Wj/eN7M4VgoYA/M2PF7uasA+IBLcPWG4c2tuAfnJ2Blw8z21a0YEFggu7ofxh/KkuYCmozLEHNMtbevBhy3Tvb6sEkGmdAasHIbPJ4OKINsBo92Gspd9iYskLi9oR0ColI8+XXRwztaLiKaNj+YGxNjvBA7fKPV9E1YEyZNyOA3X1FBV1LI9CMydLDz8O7eeLkgQ6eFnKQgUD3NVzg3JXwdgdLSdg8TR1i8kcU6c0vgccBe1o4SCdKYTae6Md3VFGAyhG4CAwMlrmDGcEMIKWiqkJncDT7EcLYdUyA68e/HsWgvGLzUgqEpyDZDCVjE5pEA9GYgs9/zMYiS2QjkSfTwVT3MLL1cDQgaWgDriDCkivAHrGADIZANdKAjC6PtbKCmQgYzzRZnflykjjt/dyb9dyZQ395cX2SbS+A3q2NlbdBVioRku9Xry3GXc75euXqWnRD6YI09Z4y33QGXsjQ8TbXrJH9FOIq2qXNb1wWhLpPlVQ9yOp8Q6GrL7md3seyiNapyjIigURVBBBBRFUEEEFEVQEFUTQu5KWC/9QF0z7t0xmyJzQnS+Z+xELao16MqIRd1qFPGo96vcUzR0di0p3YNxYlxdP8cd88ZQgCIIgCIIgCIIgCIIgCIIgCIIgCIIgMLShsnyWLlfmUWPpZ7IuVxAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEQRAEgSf7g18whv93o/Z18Su/cF4N+aktq2/vKKgrVhx6QceKV8dd/3KzPvTnFpj5hrsEhNViVc/Qn3R1rHRVeJjPtacQNUb7/Pu7CBr3OGroz9kpxQtXtcQ/PwE9az8v3CUQj05JPQHvIM0Vr/6Y6QSegusT6Mzc6aUZ8adw0iUkmN2TIi6CPi3EQsVCRVCxUB5dYMrfZQhhgf5Rz9kE4z4ttPVwJxSC2hV764HarTMPs4Walu7DMj+memIp4QyLhabToV+pFgLLPRG6Qs+0mQ49KQs1MyMnZzF/rXyzjVr2u0zBGAoL1abKWyFtcIYiNNGBZz9o9Svs033iJlR7OhZqZhu7Z+PsN10mpukApoPZs9fe396f8nD0oaHcd5tOrm+XhEJoM1Vf/dxSgVD3b+g83nIo1N8VGnJBzUynNen95X3GZWPSbXktE0ynq6Np9v9AbDi83PoIM/ywcKFM6EVrkxeA9qJGCEIaNTTmqYVCNZpfNy+ud6j2sNf8d2hyg3vBV8AaeiZotlsFU0uGt1Juz7pu+aZPaNbPtFwx4Fu/7+8tjTyYR2SSGf3hjRNKu91rLfd02zFf8u1fLEXHNpffhuC5Uxr1bG68cFaXtprbOR/P3ACtNfezl9NqszbEgjocEzowAMdy7cUjWyu/eNr5UGTPcluu2G5wbGtq078/fpKP33cT+WB9aN3zLasz/Gmr7vqBLzX7G/7stpj+Lgw/wA8z+9rSNyiHv7j/r65/w5f2d5/xo5PZgzH3yQ9f/GR9/b09vE2uRQIXAEoPP9v+ZXwra9qG95cEcRaOvQe/hF7PtibeHEzbRIZlHJrjs9ym8a1Fp/tZf/9yhrH/ajl85v8zm0bue778ry/57scVrM+/3LShbvjLii/rcb52/Ym9QGh4BdUp9M9bvXydWzjBA748VR1cehk9T0P3PE+9t4whmSkK2UeoHydekHsBvAaoBQAC4Hrxfga2mdn8eXMGHRKvtboDAY1l53PNs8nf//cnNieGuMlVdDjBNBwLcuWjkFsHMEzdhJrynilA5f36yFtNG44+tP7iG77nRziq1ehLCvwcAPtnO8SM/s1W/26a2toIAHXUD1+8fAF8Bn6qQz1s0Yz6Aqa1tJCu4N3WrIuUMzODCWemZ3d3rW2Vh2Qut0Ui8PlfPmfT1OAFL+ga3Iv+GHTTwrFeWJtMdW8A4IW7rv7vxc8mrOv66mq+NsSCGoUx9qbmk+9KowQiC3VAqwPWGGMcLcRji45uxhcmng/JODTk+YGF/3jt1r9gkc/YM/+HTeqnFE0bHNhk0fsZMfOMzwIv+a7bTG00mV7uLGpfc2KaxWlCwzxsMVZX1J6lT5+8jjcaGeUBe6QBRpGXufKenjkpLNWOi06A2F6s9Pi93LqaiVfz9o/a85mfFl998S2BP5WCG021qf/JNaNATcO7z7+Hz3dzzMS3QM2szhdn3m+C9/uv//4DX6gHnNu9ajZOH/WU7nlqPq2fFdCtROIlvmiprdtgeW3HImvlMUzS+g5Gyxm/1+8dObY+2DcT/OTmbv5NiBoQqjG/EUi/0QI10Oz5/IVMobo9393/4fR9mnz9k0ctofTp5r9PUDABDBwLDFNXZnfbALP7FMYEjPt/2vIwgp4/PAlRIwS1EDV6G709hKC/8zzpfNc92Of1gv4+j896Oimju230t/sJxmCux+7l1gY3+v8ub/Tz1C7lu3y0POCWFQuyYkEEFQsVQcVCRVCxUBFULFQERQSl/wgz7wz/mTktPpxXYNNVfwqy1V3XzCv0nj3/irO4OfyKqmjpqpPIZOrW0J9bqJXI//F+wV3uXLn/69Un8Avuxf+Rdyzwx3jHgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIwu/P/wdK+m+H7BjjIAAAAABJRU5ErkJggg==)

Go ahead and pick a channel that the app will post to, then select **Authorize**. If you need to add the incoming webhook to a private channel, you must first be in that channel.

You'll be sent back to your app settings, where you should see a new entry under the **Webhook URLs for Your Workspace** section. Your webhook URL will look something like this:

```
https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

That URL is your shiny new incoming webhook, one that's specific to a single user and a single channel.

For GovSlack devs

If you're developing a [GovSlack](/govslack) app for use by public sector customers, make your API calls to the `slack-gov.com` domain instead of the `slack.com` domain.

Let's see how you can actually use that webhook to post a message.

Keep it secret, keep it safe

Your webhook URL contains a secret. Don't share it online, including via public version control repositories. **Slack actively searches out and revokes leaked secrets.**

### 4. Use your incoming webhook URL to post a message {#posting_with_webhooks}

Later in this doc we'll explain [how to make your messages more expressive or interactive](#advanced_message_formatting), but for right now anything will do, so we're going to use that old standby — "Hello, world".

Make an HTTP POST request like this:

```
POST https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXXContent-type: application/json{    "text": "Hello, world."}
```

The URL that you're making the POST request to should be the same URL you generated in the previous step.

That's it! Go and check the channel your app was installed into, and you'll see that the "Hello, World" message has been posted by your app.

You can use this in a real Slack app without much change, just substitute your favorite HTTP Request library for cURL and structure all the requests in the exact same way. You'll also need to pay attention to some details [we've outlined below](#incoming_webhooks_programmatic) when you're distributing your app.

Incoming webhooks do not allow you to delete a message after it's been posted.

If you need a more complex chat flow including message deletion, call [`chat.postMessage`](/reference/methods/chat.postMessage).

Great work, you've set up incoming webhooks for your Slack app and made a successful test call, and you're ready to start making those messages more interesting and useful. We baked some extra treats to celebrate! 🍪🍪🍪🍪

* * *

## Making it fancy with advanced formatting {#advanced_message_formatting}

Incoming webhooks conform to the same rules and functionality as any of our other messaging APIs. You can make your posted messages just a single line of text, or use [interactive components](/messaging/creating-interactive-messages).

The process of using all these extras and features is similar to [the one explained above](#posting_with_webhooks). The only difference is the JSON payload that you send to your webhook URL will contain other fields in addition to `text`. Here's a more advanced HTTP request example that you can use with the same webhook `url` that you [used above](#posting_with_webhooks):

```
POST https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXXContent-type: application/json{    "text": "Danny Torrence left a 1 star review for your property.",    "blocks": [    	{    		"type": "section",    		"text": {    			"type": "mrkdwn",    			"text": "Danny Torrence left the following review for your property:"    		}    	},    	{    		"type": "section",    		"block_id": "section567",    		"text": {    			"type": "mrkdwn",    			"text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room 237 was far too rowdy, whole place felt stuck in the 1920s."    		},    		"accessory": {    			"type": "image",    			"image_url": "https://is5-ssl.mzstatic.com/image/thumb/Purple3/v4/d3/72/5c/d3725c8f-c642-5d69-1904-aa36e4297885/source/256x256bb.jpg",    			"alt_text": "Haunted hotel image"    		}    	},    	{    		"type": "section",    		"block_id": "section789",    		"fields": [    			{    				"type": "mrkdwn",    				"text": "*Average Rating*\n1.0"    			}    		]    	}    ]}
```

This example uses [Block Kit](/block-kit) visual components to make the message more expressive and useful.

We have some fantastic docs that explain how to use [text formatting](/messaging/formatting-message-text) and [Block Kit](/block-kit) to make your messages more interesting and interactive, so please dive into [our overview of message composition](/messaging).

You **cannot override** the default channel (chosen by the user who installed your app), username, or icon when you're using incoming webhooks to post messages. Instead, these values will always inherit from the associated Slack app configuration.

* * *

## Posting your message as a reply in a thread {#threads}

You can use an incoming webhook to make your message appear as a reply in a thread. You'll need to retrieve the message `ts` value, however, as it is not returned when sending a request to an incoming webhook. You'll use the `ts` value as the `thread_ts` field of the webhook request to generate the threaded reply.

You can retrieve the `ts` value in one of the following ways:

*   Enable and use the [Events](/reference/events) API so that you can subscribe to event types that will send a callback when a new message is sent by your incoming webhook.
*   Use the [`assistant.search.context`](/reference/methods/assistant.search.context) method to search for the message you sent based on the timestamp.
*   Use the [`conversations.history`](/reference/methods/conversations.history) method to search for the message from a set of messages.

Read about [replying to messages](/messaging/sending-and-scheduling-messages#threading) and [retrieving messages](/messaging/retrieving-messages#individual_messages) for more details.

* * *

## Generating incoming webhook URLs programmatically {#incoming_webhooks_programmatic}

In the guide above, we demonstrated how to quickly generate a webhook URL through your app settings UI; however, when you're distributing your app (for use by non-collaborators), you'll need a way for it to generate those URLs on the fly.

Fortunately, incoming webhooks can be easily generated during the [standard OAuth install flow](//authentication#flow).

If you're going to [distribute your app](/app-management/distribution), it's likely you're already planning to use the OAuth process anyway. Below we'll cover the adjustments you'll need to make to that process to enable incoming webhooks.

### 1. Change your scopes {#adjust_scopes}

As part of the install process, your app defines a set of initial [permission scopes](/authentication/installing-with-oauth) to request from a user. Whether you're using the [Slack button](/legacy/legacy-slack-button#button-widget) to provide a link for users to install your app or your own [custom OAuth redirect](//authentication#step_1_-_sending_users_to_authorize_and_or_install), there will be a `scope` parameter that sets this initial list of permissions.

To generate incoming webhook URLs, make sure you include the [`incoming-webhook` permission](/reference/scopes/incoming-webhook) in that `scope` list. When you do, users will see an additional permission on the Authorize screen that allows them to pick the channel where incoming webhooks will post to, [as shown above](#create_a_webhook).

### 2. Grab incoming webhook URL from the OAuth Response {#oauth_response}

Once a user installs your app and your app has completed the [OAuth verification code exchange](//authentication#step_3_-_exchanging_a_verification_code_for_an_access_token), you'll receive a JSON response like this:

```
{    "ok": true,    "access_token": "xoxp-XXXXXXXX-XXXXXXXX-XXXXX",    "scope": "identify,bot,commands,incoming-webhook,chat:write:bot",    "user_id": "XXXXXXXX",    "team_name": "Your Workspace Name",    "team_id": "XXXXXXXX",    "incoming_webhook": {        "channel": "#channel-it-will-post-to",        "channel_id": "C05002EAE",        "configuration_url": "https://workspacename.slack.com/services/BXXXXX",        "url": "https://hooks.slack.com/TXXXXX/BXXXXX/XXXXXXXXXX"    }}
```

You can see that this OAuth response contains an `incoming_webhook` object, and right there in the `url` field is your brand new incoming webhook URL. You can now go ahead and use this URL to post a message, as [demonstrated above](#posting_with_webhooks). Here's a full explanation of all the fields in this `incoming_webhook` object:

Attribute

Type

Description

`channel`

String

The name of the channel the user selected as a destination for messages

`channel_id`

String

The ID of the same channel

`configuration_url`

String

A link to the page that configures your app within the workspace it was installed

`url`

String

The incoming webhook URL

* * *

## Handling errors {#handling_errors}

Though in most cases you'll receive a "HTTP 200" response with a plain text `ok` indicating that your message posted successfully, it's best to prepare for scenarios where attempts to publish a message will fail.

Incoming webhooks may throw errors when receiving malformed requests, when utilized webhook URLs are no longer valid, or when something truly exceptional prevents your messages from making it through to channels and users.

Incoming webhooks return more expressive errors than our Web API, including more relevant HTTP status codes (like "HTTP 400 Bad Request", "HTTP 403 Forbidden", and "HTTP 404 Not Found"). These are described in our changelog: [Changes to errors for incoming webhooks](/changelog/2016-05-17-changes-to-errors-for-incoming-webhooks).

Errors you may encounter include:

*   `action_prohibited` usually means that an admin has placed some kind of restriction on this avenue of posting messages and that, at least for now, the request should not be attempted again.
*   `channel_is_archived` indicates the specified channel has been archived and is no longer accepting new messages.
*   `invalid_payload` typically indicates that received request is malformed — perhaps the JSON is structured incorrectly, or the message text is not properly escaped. The request should not be retried without correction.
*   `invalid_token` means the token used was expired, invalid, or missing.
*   `no_active_hooks` means the incoming webhook is disabled.
*   `no_service` means the incoming webhook is either disabled, removed, or invalid.
*   `no_service_id` means the `service_id` (`B00000000` in our examples above) was either invalid or missing.
*   `no_team` means the Slack workspace was either missing or invalid.
*   `no_text` means the `text` attribute was missing from the payload. Refer to the [messages](/messaging) page for valid formatting details.
*   `posting_to_general_channel_denied` is thrown when an incoming webhook attempts to post to the "#general" channel for a workspace where posting to that channel is 1) restricted and 2) the creator of the same incoming webhook is not authorized to post there.
*   `team_disabled` means the Slack workspace is no longer active.
*   `too_many_attachments` is thrown when an incoming webhook attempts to post a message with greater than 100 attachments. A message can have a maximum of 100 attachments associated with it.
*   `user_not_found` and `channel_not_found` indicate that the user or channel being addressed either do not exist or are invalid. The request should not be retried without modification or until the indicated user or channel is set up.

## Triggering workflows with webhooks {#workflows}

See the help center article [Build a workflow: Create a workflow that starts outside of Slack](https://slack.com/help/articles/360041352714-Build-a-workflow--Create-a-workflow-that-starts-outside-of-Slack).