# SECURITY.md

## 1. OWASP risk for unauthenticated list view
If the incident list has no authentication and exposes all records, it falls under Broken Access Control (OWASP A01). Attackers could access sensitive information without authorization.

## 2. What CSRF token prevents
CSRF tokens prevent Cross-Site Request Forgery attacks. Without the token, an attacker could force a logged-in user to submit malicious requests.

## 3. What IDOR is
IDOR (Insecure Direct Object Reference) happens when users can access objects by modifying identifiers such as IDs. If incidents belonged to users and ownership checks were missing, an attacker could change URLs like:

/incidents/1/
/incidents/2/
/incidents/3/

and access other users' incidents.

## 4. What is mass assignment
Mass assignment occurs when attackers send unexpected fields to modify protected values. Limiting ModelForm fields prevents users from changing fields they should not control.

## 5. Why GET-based deletion is dangerous
Deletion through GET is dangerous because attackers could trigger actions without user consent using CSRF attacks.

## 6. Bonus SQL Injection URL
If raw SQL string formatting were used:

/incidents/?severity=' OR '1'='1