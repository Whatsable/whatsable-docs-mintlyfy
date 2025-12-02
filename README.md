# WhatsAble Documentation

> Enterprise-grade WhatsApp automation solutions documentation built with [Mintlify](https://mintlify.com)

This repository contains the complete documentation for the WhatsAble suite of products—a comprehensive WhatsApp automation platform that enables businesses to automate their communication workflows through multiple integration options.

## 📚 About WhatsAble

WhatsAble provides enterprise-grade WhatsApp automation solutions for business communication. The platform offers three specialized products designed to meet different business needs:

### 🟢 WhatsAble
**Internal Communication Solution**
- **Best For**: Internal teams and small businesses
- **Features**: Unlimited messaging, team notifications, business alerts
- **Identity**: WhatsAble branding
- **Pricing**: Subscription-based
- **Dashboard**: [https://dashboard.whatsable.app](https://dashboard.whatsable.app/signin)

### 🔵 Notifier by WhatsAble
**Starter Automation Solution**
- **Best For**: Professional businesses starting with automation
- **Features**: Message analytics, open tracking, custom notifications
- **Identity**: Notifier branding
- **Pricing**: Subscription or Pay-as-you-go
- **Dashboard**: [https://notifier.whatsable.app](https://notifier.whatsable.app/sign-up)

### 🟣 Notifier System
**Enterprise Communication Solution**
- **Best For**: Professional businesses with own brand
- **Features**: Real-time chat, brand messaging, two-way communication
- **Identity**: Your business branding
- **Pricing**: Enterprise pricing (Subscription or Pay-as-you-go)
- **Dashboard**: [https://console.notifyer-systems.com](https://console.notifyer-systems.com/sign-in)

## 🚀 Features

- **Multiple Integration Options**: Connect via Zapier, Make (formerly Integromat), n8n, or direct API access
- **Comprehensive API Documentation**: Complete OpenAPI specifications for all three products
- **No-Code Solutions**: Step-by-step guides for non-technical users
- **Developer-Friendly**: RESTful APIs with detailed documentation and code examples
- **Real-time Updates**: Webhook support for message delivery and responses
- **Template Management**: Create and manage approved message templates
- **Analytics & Tracking**: Monitor delivery rates, open rates, and engagement metrics

## 📁 Project Structure

```
whatsable-docs-mintlyfy/
├── api-reference/          # API documentation
│   ├── endpoint/           # Endpoint-specific guides
│   ├── websocket-api/      # WebSocket API documentation
│   └── introduction.mdx    # API overview
├── guides/                 # Product guides and tutorials
│   ├── whatsable/         # WhatsAble product guides
│   ├── notifier/          # Notifier product guides
│   ├── notifier-system/   # Notifier System guides
│   ├── error-handling.mdx
│   ├── rate-limits.mdx
│   └── webhooks.mdx
├── openapi/               # OpenAPI specification files
│   ├── whatsable-api.json
│   ├── notifier-api.json
│   └── notifier-system-api.json
├── images/                # Documentation images and assets
├── logo/                  # Brand logos (light/dark variants)
├── snippets/              # Reusable documentation snippets
├── docs.json              # Mintlify configuration
├── index.mdx              # Homepage
├── introduction.mdx      # Main introduction page
├── quickstart.mdx         # Quick start guide
├── authentication.mdx     # Authentication guide
├── development.mdx        # Development setup guide
└── README.md             # This file
```

## 🛠️ Development Setup

### Prerequisites

- **Node.js**: Version 19 or higher
- **npm** or **yarn**: Package manager
- **Mintlify CLI**: Will be installed globally

### Installation

1. **Install Mintlify CLI globally**:

   ```bash
   npm i -g mintlify
   ```

   Or using yarn:

   ```bash
   yarn global add mintlify
   ```

2. **Navigate to the project directory**:

   ```bash
   cd whatsable-docs-mintlyfy
   ```

3. **Start the development server**:

   ```bash
   mintlify dev
   ```

   The documentation will be available at `http://localhost:3000` by default.

### Custom Port

To run on a different port:

```bash
mintlify dev --port 3333
```

If the default port is in use, Mintlify will automatically use the next available port.

### Updating Mintlify

To ensure you're using the latest version:

```bash
npm i -g mintlify@latest
```

Or with yarn:

```bash
yarn global upgrade mintlify
```

## 📝 Documentation Structure

### Guides Tab

The documentation is organized into the following sections:

1. **Get Started**
   - Introduction
   - Quickstart
   - n8n Overview

2. **WhatsAble**
   - Zapier Integration
   - Make Integration
   - n8n Integration
   - API Documentation

3. **Notifier by WhatsAble**
   - Zapier Integration
   - Make Integration
   - n8n Integration
   - API Documentation

4. **Notifyer System**
   - Embedding Process
   - Zapier Overview
   - Make Overview
   - n8n Overview
   - Pipedrive Overview
   - API Documentation
     - Get Templates
     - Template Message
     - Non-Template Message
     - Incoming Message

### API Reference Tab

- **WhatsAble API**: Complete OpenAPI documentation
- **Notifier API**: Complete OpenAPI documentation
- **Notifier System API**: Complete OpenAPI documentation

## 🔧 Configuration

The main configuration file is `docs.json`, which includes:

- **Theme**: Mint theme with custom colors (green primary: `#16A34A`)
- **Navigation**: Structured navigation with tabs and groups
- **Branding**: Custom logos for light/dark modes
- **Footer**: Social media links (X/Twitter, GitHub, LinkedIn)
- **Homepage**: Set to `introduction.mdx`

## 📖 Writing Documentation

### File Format

All documentation files use the `.mdx` format, which allows:

- Standard Markdown syntax
- React components (Card, CardGroup, Steps, etc.)
- Custom styling with Tailwind CSS classes
- Interactive elements

### Code Formatting

We recommend using:

- **MDX VSCode Extension**: For syntax highlighting
- **Prettier**: For code formatting

### Validating Links

Check for broken links:

```bash
mintlify broken-links
```

## 🚢 Deployment

### Automatic Deployment

The documentation is automatically deployed when changes are pushed to the default branch (usually `main`). This is handled by the Mintlify GitHub App.

### Manual Deployment

1. Ensure all changes are committed and pushed
2. The Mintlify GitHub App will automatically detect changes
3. Deployment status can be checked in the Mintlify dashboard

### Deployment Status

A successful deployment will show:

```
✓ Checks passed
```

## 🐛 Troubleshooting

### Mintlify dev isn't running

If the development server fails to start:

```bash
mintlify install
```

This will re-install dependencies.

### Page loads as a 404

Ensure you're running the command in the directory containing `docs.json`:

```bash
cd whatsable-docs-mintlyfy
mintlify dev
```

### Error: Could not load the "sharp" module

This is typically due to an outdated Node.js version:

1. Remove Mintlify: `npm remove -g mintlify`
2. Upgrade to Node.js v19 or higher
3. Reinstall Mintlify: `npm install -g mintlify`

### Unknown errors

If you encounter unexpected errors:

1. Delete the `~/.mintlify` folder
2. Run `mintlify dev` again

## 🔗 Resources

### Official Links

- **WhatsAble Website**: [https://www.whatsable.app](https://www.whatsable.app)
- **Pricing**: [https://www.whatsable.app/pricing](https://www.whatsable.app/pricing)
- **Documentation**: [https://docs.whatsable.app](https://docs.whatsable.app)

### Social Media

- **X (Twitter)**: [@whatsable](https://x.com/whatsable)
- **GitHub**: [@whatsable](https://github.com/whatsable)
- **LinkedIn**: [WhatsAble](https://linkedin.com/company/whatsable)

### Support

- **Email**: [team@whatsable.app](mailto:team@whatsable.app)
- **Video Tutorials**: [YouTube Channel](https://www.youtube.com/@nocodeshare/videos)
- **Consultation**: [Book a Free Consultation](https://tidycal.com/axelmeta/whatsapp-notifications-by-whatsable)

## 📄 License

This documentation is proprietary and belongs to WhatsAble. All rights reserved.

## 🤝 Contributing

For documentation improvements or corrections, please:

1. Create an issue describing the change
2. Submit a pull request with the proposed changes
3. Ensure all links are valid using `mintlify broken-links`

## 📚 Additional Documentation

- **Mintlify Documentation**: [https://mintlify.com/docs](https://mintlify.com/docs)
- **Mintlify CLI Changelog**: [https://www.npmjs.com/package/mintlify?activeTab=versions](https://www.npmjs.com/package/mintlify?activeTab=versions)

---

**Built with ❤️ using [Mintlify](https://mintlify.com)**
