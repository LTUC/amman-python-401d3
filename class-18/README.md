# Cryptography

Keeping secrets with Cryptography.

#### Describe and Define

- Cryptography
- Cryptoanalysis
- Encrypt vs. encipher
- Decrypt vs. decipher

#### Execute

- Implement Caesar cipher
- Decipher message with brute force attack
- Utilize a corpus automate deciphering

## Today's Outline

- Intro - Nizar, Noura
- Lab Review
- Break
- Lab Preview
- Lecture
- Demo
- Code Challenge Preview

## Notes
 - We want to keep secrets
 - Sending private messages
    - Pre-shared key
 - War times, communication strategy i.e. troop positions or attack plans
 - Planning a surprise

## Cracking for dummies

 In our encryption scheme we had 10 possible keys

 It would be easy for a computer to decrypt the message with every possible key. This is called "brute forcing".

 To successfully brute force we need to be able to check if the result was correct.

 An encryption system is usually secured in a few ways

 Having a large key space i.e. have so many possible keys that it takes the fastest computers longer than the age of the universe to check each one.

 Some algorithms are slow to check if correct (decrypt) on purpose to frustrate an attacker.

 Math behind the algorithm needs to be crypto secure. 
 When using random numbers in security we need to use 'real' random numbers not psuedo-randoms

 random libraries in most languages including python use psuedo randoms
 function(a, seed) -> x
 
 To get real random number we rely on some event that occurs outside of the computer
 Think outside of the box!
 Radioactive decay
 Measure how the user moves the mouse or timing for typing on the keyboard etc.
 Look into
```python
 os.urandom
 ```

## Let's get Cracking!

### which one is English? How do we know?
"a dark and stormy night"
"n quex naq fgbezl avtug"

To Check if the text result was correct we need to know what correct text looks like!

For the computer we can get a dataset of valid words and check against that.

If we count each valid english word in the sentence and make a ratio between the total words in the sentence we come up with a score of how likely the sentence is to be in english.

"I think that Dario's hair needs cutting lol but don't tell him I said that :P" , 87%

### Hashing

We want to store a secret in a way where it cannot easily be recovered BUT that we can check if another value was the same secret.

- Use Cases
  - Password
    - We store a hash as a string instead of the password string itself so that if the database gets leaked the user's password is not easily disclosed
  - Message verifying - JWT, Downloads
    - You generate a hash from a message and include it as a separate message then the receiver can verify the message by generating the hash form the message the received and checking that it matches the hash you sent

Issues with hashing
- If output 32bit but input can be any length how can we prevent two different values form having the same hash?
- Hashes are not unique!, but are likely to give unique values for the expected inputs
- A collision is when two inputs result in the same output "String 1" and "Some other string two" => hashx

Properties of a good hash function

- Has no inverse function i.e. no decrypt function no function exists g(x) such that g(f(x)) => x
- Collision resistant h(x) != h(y) when x != y for common vlaues of x, y
- Fast to encrypt slow to decrypt
- Large output space

Hashing Algorithm,
- MD4, MD5
- SHA-1, SHA-256

## Resources

[Cipher Drawing](https://replit.com/@dariothornhill/cipher#cipher.draw)

[Natural Language Toolkit Library](https://www.nltk.org/)
