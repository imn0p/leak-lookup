# leak-lookup

**Leak Lookup API Search Tool**

`leak-lookup` is a command-line tool that interacts with the [leak-lookup.com](https://leak-lookup.com) API to perform searches on various types of data. You can use this tool to search for information based on email addresses, usernames, IP addresses, phone numbers, domains, passwords, and full names.

## Features

- **Type-Based Search**: Conduct detailed searches using different data types, including email addresses, usernames, IPs, phone numbers, domains, passwords, and full names.
- **API Key Storage**: Configure your API key once for future use.
- **Command-Line Interface**: Use a simple command-line interface to execute searches.

## Installation

To install `leak-lookup`, follow these steps:

1. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/imn0p/leak-lookup.git
    ```

2. Navigate into the `leak-lookup` directory:
    ```bash
    cd leak-lookup
    ```

3. Configure your API key for future use:
    ```bash
    python3 leak-lookup --config <api-key>
    ```
    This will store your API key locally, ensuring that it is kept secure and not shared with anyone.

## Available Types

You can perform searches using the following data types:

- **email_address**: Search by email address.
- **username**: Search by username.
- **ipaddress**: Search by IP address.
- **phone**: Search by phone number.
- **domain**: Search by domain.
- **password**: Search by password.
- **fullname**: Search by full name.

