# What is API documentation

This is an introduction to APIs for beginners. If you've ever created or documented an API, you don't need to read it.

If you're trying to understand what APIs do, and why everyone is documenting them -- this page is for you.

I wrote this because so many people ask me how technical writing works, and how they can get into it.

## An API is a set of custom commands

An _application programming interface_ (API) is a term to describe the methods that a program contains to allow other programs to talk to it. When software includes an API, newer programs, created by people other than the author of the original software can talk to it.

For example, anyone who can write an app can use the twitter API to extract tweets and display them, or can submit tweets on behalf of a user.

Some APIs are also called services or libraries, because they contain useful tools, designed for no purpose other than being included into your work. In other words, a library might have no function other than to be a part of a larger program, if it performs one small task that is not useful by itself.

APIs are tremendously helpful to programmers because when they rely on an API to perform certain functions, they save a lot of time by not having to write all the code that would perform that function.

But to take advantage of APIs, you have to follow their rules. An API makes certain commands available to accomplish certain tasks -- but only if you use them the right way. The commands are unique within any API -- and that's why they need to be documented. The API documentation is a little bit like a dictionary (although not exactly), because its main purpose is to let you know all the commands that are available to you, and what they will do.

## Who uses API documentation

Knowing what APIs are, it should make sense that the API documentation is consumed mostly by developers. Sometimes the API documentation is written by the developer who created the API, sometimes it is written by a documentation specialist. There is software that can generate a very simple API reference for an API -- although it doesn't tell you everything that you might want to know.

## What is included?

API documentation, at the very least, should include all the commands available (or methods, or endpoints, depending on what you want to call them). It also must explain the parameters that go with each endpoint; if the user is required to supply two pieces of input to make a service work properly, someone must explain the inputs that are required, restrictions on the content (text or numerals only, length), and where to send the data (a URL or function that receives it and then responds)

 But developers often also need help to understand the workflow -- a set of steps designed to complete a complex task, which might require them to use a series of services one at a time.
