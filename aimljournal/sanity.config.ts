import {defineConfig} from 'sanity'
import {structureTool} from 'sanity/structure'
import {visionTool} from '@sanity/vision'
import {schemaTypes} from './schemas'
import { codeInput } from '@sanity/code-input'; // Import codeInput

export default defineConfig({
  name: 'default',
  title: 'aimljournal',

  projectId: 'ugsaokcj',
  dataset: 'production',

  plugins: [structureTool(), visionTool(), codeInput()],

  schema: {
    types: schemaTypes,
  },
})
