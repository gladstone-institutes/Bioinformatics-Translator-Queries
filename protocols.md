# Protocols

## Main process for running core queries
1. Go to https://arax.ncats.io/
2. To create the query either:
    - Use the query graph builder, then click **Show JSON in Status window**, and copy the JSON
    - Or paste in JSON in the JSON input field
4. Record the query JSON and save to Dropbox.
5. Click **Query ARS**.
6. When results load, record the URL for ALL results as **Query results**.
7. For BTE results:
   - Click on the BTE results link
   - Click on **Messages** tab in the left-hand side bar
   - Copy the results URL at the top of the message, save this as **BTE JSON**
   - Open the results link in a separate tab, copy the contents and save as a json file in Dropbox, titled using the alphanumeric part of the results URL, for example "MU2ufjDuJa" for https://bte.transltr.io/v1/asyncquery_response/MU2ufjDuJa.

## Running BTE queries in the ARAX interface
1. Go to https://arax.ci.transltr.io/ or https://arax.ncats.io/
2. Click on the JSON icon, then click **Settings**
3. Update the **external API** url: 
   - Dev: https://api.bte.ncats.io/v1
   - CI: https://bte.ci.transltr.io/v1
   - test: https://bte.test.transltr.io/v1
   - prod: https://bte.transltr.io/v1"
4. Click **Update** button next to External API input
5. Format the query using the graphical query builder, or paste in JSON
6. When you're ready to submit your query, click the button **Post to OTHER** or **Query OTHER** button the **Queries** tab.
7. To record the results: Copy the URL

## Running MVP1/MVP2 queries in Translator UI
1. Go to https://ui.transltr.io/ and login
2. Run any MVP1 or MVP2 query.
3. To record the results: Click on the **Share Results Set** button and copy the link

## Running PathFinder queries in PathFinder Translator UI
1. Go to https://ui.ci.transltr.io/pathfinder and login
2. Format your query, adding any intermediary nodes by clicking the **+ Middle Object** button. 
3. To record the results: Click on the **Share Results Set** button and copy the link
